from django.shortcuts import render

from .models import Product
import requests
from .shopify_secrets import SHOPIFY_CLIENT_ID, SHOPIFY_CLIENT_SECRET

def fetch_shopify_products():
	# Replace with your actual shop name and access token
	SHOP_NAME = 'carrylux'
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
	if not products:
		# Hardcoded sample products
		class HardProduct:
			def __init__(self, name, description, price, created_at):
				self.name = name
				self.description = description
				self.price = price
				self.created_at = created_at

		products = [
			HardProduct("Gucci Marmont", "Iconic designer shoulder bag in quilted leather.", 2499.99, "2025-08-01"),
			HardProduct("Prada Re-Edition", "Trendy nylon mini bag with classic logo.", 1299.00, "2025-08-05"),
			HardProduct("Louis Vuitton Neverfull", "Spacious tote with signature monogram canvas.", 1899.50, "2025-08-10"),
			HardProduct("Chanel Classic Flap", "Timeless lambskin bag with gold hardware.", 3999.00, "2025-08-15"),
		]
	return render(request, 'shop/product_list.html', {'products': products})

def categories(request):
	return render(request, 'categories.html')
