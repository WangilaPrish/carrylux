from django.shortcuts import render

from .models import Product
import requests
from .shopify_secrets import SHOPIFY_CLIENT_ID, SHOPIFY_CLIENT_SECRET

def fetch_shopify_products():
	# Replace with your actual shop name and access token
	SHOP_NAME = 'your-shop-name'
	ACCESS_TOKEN = SHOPIFY_CLIENT_SECRET  # Typically, you need an OAuth token, not just the secret
	url = f'https://{SHOP_NAME}.myshopify.com/admin/api/2023-04/products.json'
	headers = {
		'X-Shopify-Access-Token': ACCESS_TOKEN,
		'Content-Type': 'application/json'
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		return response.json().get('products', [])
	return []

from django.shortcuts import render
from .models import Product


def landing(request):
	return render(request, 'landing.html')

def about(request):
	return render(request, 'about.html')

def product_list(request):
	products = Product.objects.all()
	return render(request, 'shop/product_list.html', {'products': products})

def categories(request):
	return render(request, 'categories.html')
