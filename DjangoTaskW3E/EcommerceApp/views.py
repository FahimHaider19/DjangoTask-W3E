from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Product

# Create your views here.

class views:

    def home(request):
        return HttpResponse("Hello World")
    
    def product(request, id):
        try:
            product = Product.objects.get(pk=id)
            return HttpResponse(product)
        except Product.DoesNotExist:
            raise Http404("Product does not exist")
    
    def products(request):
        products = [{
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'publisher': product.publisher,
            'developer': product.developer,
            'image': product.image,
            'titleimage': product.titleimage,
        } for product in Product.objects.all()]

        return HttpResponse(products)