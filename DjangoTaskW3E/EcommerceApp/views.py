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
            
            # print(reviews, product)
            return render(request, 'product.html', { 'product': product, 'reviews': reviews })
        except Product.DoesNotExist:
            raise Http404("Product does not exist")
    
    def products(request):            
        search_query = request.GET.get('search', '')
        products = []
        msg = None

        if search_query and len(search_query) > 2:
            products = Product.objects.filter(name__icontains=search_query)
        elif search_query and len(search_query) <= 2:
            msg = "Query length should be at least 3 characters"
            products = Product.objects.all()
        else:
            products = Product.objects.all()

        # product_list = [
        #     {
        #         'name': product.name,
        #         'price': product.price,
        #         'description': product.description,
        #         'publisher': product.publisher,
        #         'developer': product.developer,
        #         'image': product.image,
        #         'titleimage': product.titleimage,
        #     }
        #     for product in products
        # ]
        return render(request, 'products.html', {'products': products, 'msg': msg})
    
    def addReview(request, name):
        if request.method == 'POST':
            product = Product.objects.get(name=name)
            if not product:
                raise Http404("Product does not exist")
            elif request.POST['user'] == '' or request.POST['review'] == '' or request.POST['rating'] == '':
                return HttpResponse("Please fill all the fields")
            product.reviews.create(user=request.POST['user'], text=request.POST['review'], rating=request.POST['rating'])
            return render(request, 'product.html', { 'product': product, 'msg': 'Review added successfully' })