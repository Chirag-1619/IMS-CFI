import os
import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from cif.models import Customer

class Command(BaseCommand):
    help = 'Import customer data from CSV file'

    def handle(self, *args, **kwargs):
        file_name = r'C:\Users\moksh\OneDrive\Desktop\CIF\cif_project\customer_data.csv'  # Change the file path if necessary

        with open(file_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            imported_contacts = []  # List to keep track of imported customer contacts

            for row in reader:
                try:
                    amc_upto_date = datetime.strptime(row['AMC_Upto_Date'], '%d/%m/%Y').strftime('%Y-%m-%d')
                    date_of_installation = datetime.strptime(row['Date_of_Installation'], '%d/%m/%Y').strftime('%Y-%m-%d')
                except ValueError:
                    self.stdout.write(self.style.WARNING(f"Skipping row: {row} due to invalid date format."))
                    continue

                # Check if a customer with the same details already exists
                existing_customer = Customer.objects.filter(
                    name=row['Name'],
                    address=row['Address'],
                    contact=row['Contact'],
                    machine_model=row['M/c Model'],
                    date_of_installation=date_of_installation,
                    amc_status=row['AMC_Status'],
                    amc_upto_date=amc_upto_date,
                ).first()

                if existing_customer:
                    # Skip updating the customer if they already exist
                    self.stdout.write(self.style.WARNING(f"Customer {row['Name']} already exists. Skipping update."))
                else:
                    # Create a new customer record
                    customer = Customer(
                        name=row['Name'],
                        address=row['Address'],
                        contact=row['Contact'],
                        machine_model=row['M/c Model'],
                        date_of_installation=date_of_installation,
                        amc_status=row['AMC_Status'],
                        amc_upto_date=amc_upto_date,
                    )
                    customer.save()
                    imported_contacts.append(customer.contact)  # Add contact to the list
                    self.stdout.write(self.style.SUCCESS(f"Customer {row['Name']} imported successfully."))

            # Delete the customers that were not imported from the CSV file
            if imported_contacts:
                deleted_customers = Customer.objects.exclude(contact__in=imported_contacts)
                deleted_customers.delete()
        self.stdout.write(self.style.SUCCESS('Customer data import completed.'))


