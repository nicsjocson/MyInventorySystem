from django.shortcuts import render
from .models import Supplier

# Create your views here.
def hello_world(request):
    return render(request, 'MyInventoryApp/hello_world.html')

def view_supplier(request):
        supplier_objects = Supplier.objects.all()
        return render(request, 'MyInventoryApp/view_supplier.html', {'suppliers':supplier_objects})

def view_bottles(request):
    return render(request, 'MyInventoryApp/view_bottles.html')

def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html')