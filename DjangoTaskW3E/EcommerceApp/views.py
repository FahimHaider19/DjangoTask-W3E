from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Product

# Create your views here.

class views:

    def home(request):
        return HttpResponse("Hello World")
    
    def product(request, name):
        try:
            product = Product.objects.get(name=name)
            reviews = [{
                    'user': review.user,
                    'text': review.text,
                    'rating': review.rating
                } for review in product.reviews.all()]
            
            print(reviews, product)
            return render(request, 'product.html', { 'product': product, 'reviews': reviews })
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
        print(products)
        return render(request, 'products.html', {'products': products})
    
    def addReview(request, name):
        if request.method == 'POST':
            product = Product.objects.get(name=name)
            product.reviews.create(user=request.POST['user'], text=request.POST['review'], rating=request.POST['rating'])
            return HttpResponse("Review added")