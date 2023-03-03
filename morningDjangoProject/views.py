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
            messages.error(request, 'Account creation failed')
            return redirect("register")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
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

@login_required
def view_products(request):

    #select all the products from the database
    products = Product.objects.all()

    #render the template with the prodicts
    return render(request, 'products.html', {'products': products})

@login_required
def delete_product(request, id):
    #select the product to delete
    product = Product.objects.get(id=id)
    #finally delete the product
    product.delete()
    #redirect back to product page with a success message
    messages.success(request, 'Product deleted successfully')
    return redirect('products')

@login_required
def update_product(request,id):
    #select the product to be updated
    product = Product.objects.get(id=id)

    #check if the form has any submitted records to recieve them
    if request.method == "POST":
        updated_name = request.POST.get('jina')
        updated_quantity = request.POST.get('kiasi')
        updated_price = request.POST.get('bei')

        #update the selected product above with the recieved data
        product.prod_name = updated_name
        product.prod_quantity = updated_quantity
        product.prod_price = updated_price

        #return the updated data back to the database
        product.save()

        #redirect back to the products page with a success message
        messages.success(request, 'Product updated successfully')
        return redirect('products')

    return render(request, 'update-product.html', {'product': product})
