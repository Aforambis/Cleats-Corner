from django.shortcuts import render, get_object_or_404
from .models import Product

def list_of_products(request):
    products = Product.objects.all()
    return render(request, "list_of_products.html", {"products": products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    sizes = product.sizes.all()
    return render(request, "product_details.html", {"product": product, "sizes": sizes})