from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Account, Supplier, WaterBottle 

# ==========================================
#      NEW MODULE 6 ACCOUNT VIEWS
# ==========================================

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        # Check if credentials are valid
        account = Account.objects.filter(username=u, password=p).first()
        if account:
            # We save the account ID securely in the browser's "session"
            # because view_supplier doesn't have an <int:pk> in its URL!
            request.session['account_id'] = account.pk 
            return redirect('view_supplier')
        else:
            messages.error(request, "Invalid login")
            
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        if Account.objects.filter(username=u).exists():
            messages.warning(request, "Account already exists")
        else:
            Account.objects.create(username=u, password=p)
            messages.success(request, "Account created successfully")
            return redirect('login')
            
    return render(request, 'signup.html')

def logout_view(request):
    # This erases the saved session memory to log the user out
    request.session.flush() 
    return redirect('login')

def manage_account_view(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'manage_account.html', {'account': account})

def change_password_view(request, pk):
    account = get_object_or_404(Account, pk=pk)
    
    if request.method == 'POST':
        curr_p = request.POST.get('current_password')
        new_p = request.POST.get('new_password')
        confirm_p = request.POST.get('confirm_password')
        
        if curr_p == account.getPassword() and new_p == confirm_p and new_p != "":
            account.password = new_p
            account.save()
            return redirect('manage_account', pk=pk)
        else:
            messages.error(request, "Invalid current password or new passwords do not match.")
            
    return render(request, 'change_password.html', {'account': account})

def delete_account_view(request, pk):
    account = get_object_or_404(Account, pk=pk)
    account.delete()
    return redirect('logout')

# ==========================================
#      INVENTORY VIEWS
# ==========================================

def view_supplier(request):
    # We grab the ID out of the session so the "Manage Account" button knows who is logged in
    account_id = request.session.get('account_id') 
    suppliers = Supplier.objects.all()
    return render(request, 'view_supplier.html', {'suppliers': suppliers, 'account_id': account_id})

def view_bottles(request):
    bottles = WaterBottle.objects.all()
    return render(request, 'view_bottles.html', {'bottles': bottles})

def view_bottle_details(request, pk):
    bottle = get_object_or_404(WaterBottle, pk=pk)
    return render(request, 'view_bottle_details.html', {'bottle': bottle})

def add_bottle(request):
    if request.method == 'POST':
        # Grab the user's input from the HTML form
        b_name = request.POST.get('bottle_name')
        supplier_id = request.POST.get('supplier_id')
        
        # Find the actual Supplier object from the database using the dropdown's ID
        selected_supplier = get_object_or_404(Supplier, pk=supplier_id)
        
        # Save the new bottle to the database!
        WaterBottle.objects.create(name=b_name, supplier=selected_supplier)
        return redirect('view_supplier')
        
    # If it's a GET request, just show the form with the supplier dropdown
    suppliers = Supplier.objects.all()
    return render(request, 'add_bottle.html', {'suppliers': suppliers})