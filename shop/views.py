from django.shortcuts import render
from .models import Product

from django.shortcuts import render
from .models import Product

def landing(request):
	return render(request, 'landing.html')

def product_list(request):
	products = Product.objects.all()
	return render(request, 'shop/product_list.html', {'products': products})
