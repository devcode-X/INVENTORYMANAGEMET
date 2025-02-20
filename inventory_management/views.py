# from django.shortcuts import render, get_object_or_404
# from inventory.models import Product

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product_list.html', {'products': products})

# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'product_detail.html', {'product': product})
# # templates\inventory\product_detail.html
# def restock_product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     if request.method == 'POST':
#         restock_quantity = int(request.POST.get('quantity', 0))
#         product.quantity += restock_quantity
#         product.save()
#         return render(request, 'restock_product.html', {'product': product, 'success': True})
#     return render(request, 'restock_product.html', {'product': product})
from django.shortcuts import render, get_object_or_404, redirect
from inventory.models import Product
from django.contrib.auth.decorators import login_required, user_passes_test

# Check if the user is a superuser
def is_admin(user):
    return user.is_superuser
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
@login_required
@user_passes_test(is_admin)
def restock_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity"))
        product.stock += quantity
        product.save()
        return redirect("product_list")
    return render(request, "restock_product.html", {"product": product})
