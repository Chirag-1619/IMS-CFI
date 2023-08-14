# cif/admin.py


from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact', 'machine_model', 'date_of_installation', 'amc_status', 'amc_upto_date')
    list_filter = ('amc_status',)  # Add a filter for AMC Status
    search_fields = ('name', 'address', 'contact')
admin.site.register(Customer, CustomerAdmin)
