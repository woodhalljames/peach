from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
	products = Product.objects.all().filter(in_stock=True).order_by('-created_date')
	#.filter(in_stock=True) shows and imports only products in stock. may want to keep on site but show out of stock. 

	for product in products: 
		reviews = ReviewRating.objects.filter(product_id=product.id, status = True)

	context = {
		'products': products, 
		}
	return render(request, 'home.html', context)
