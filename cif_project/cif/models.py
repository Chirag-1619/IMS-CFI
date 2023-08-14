from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    machine_model = models.CharField(max_length=50)  # M/c Model
    date_of_installation = models.DateField(default='1970-01-01')  # DOI
    amc_status_choices = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    amc_status = models.CharField(max_length=10, choices=amc_status_choices, null=True)
    amc_upto_date = models.DateField(blank=True, null=True)  # AMC Upto Date
