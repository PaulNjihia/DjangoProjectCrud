from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect("register")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})

@login_required
def home(request):
    return render(request, 'home.html')

def add_product(request):
    if request.method =="POST":
        p_name = request.POST.get("jina")
        p_quantity = request.POST.get("kiasi")
        p_price = request.POST.get("bei")
        product = Product(prod_name= p_name, prod_quantity=p_quantity, prod_price=p_price)
        product.save()
        messages.success(request, 'Product saved successfully')
        return redirect('add-product')
    return render(request, 'add-product.html')
