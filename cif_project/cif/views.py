from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm  # Assuming you have a CustomerForm defined in forms.py



def dashboard(request):
    if request.user.is_authenticated:
        customers = Customer.objects.all()
        return render(request, 'dashboard.html', {'customers': customers})
    else:
        return render(request, 'login.html')

from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm  # Assuming you have a CustomerForm defined in forms.py


def homepage(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        category = request.POST.get('category', 'name')  # Get the selected category from the form
        # Perform the search based on the selected category and search query
        if category == 'name':
            customers = Customer.objects.filter(name__icontains=search_query)
        elif category == 'address':
            customers = Customer.objects.filter(address__icontains=search_query)
        elif category == 'branch_code':
            customers = Customer.objects.filter(branch_code__icontains=search_query)
        # Add more conditions for other fields as needed
    else:
        customers = Customer.objects.all()

    return render(request, 'homepage.html', {'customers': customers})

from django.shortcuts import render

def your_view(request):
    return render(request, 'your_template.html', {})



def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')  # Redirect to a success page or the home page
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})


def search_customers(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        customers = Customer.objects.filter(name__icontains=search_query)
        # You can add more filters based on other fields as needed
    else:
        customers = Customer.objects.all()

    return render(request, 'homepage.html', {'customers': customers})