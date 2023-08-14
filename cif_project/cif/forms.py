from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'contact', 'machine_model', 'date_of_installation', 'amc_status', 'amc_upto_date']
