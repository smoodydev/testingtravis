from django.shortcuts import render
from products.models import Product

# Create your views here.

# create a method called do_search

def do_search(request):
  products = Product.objects.filter(name__icontains = request.GET['q'])
  return render(request, 'products.html', {'products':products})



