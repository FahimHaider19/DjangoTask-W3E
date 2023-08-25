from django.urls import path
from django.conf import settings
from .views import views
from django.conf.urls.static import static

app_name = 'EcommerceApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.products, name='products'),
    path('product/<name>', views.product, name='product'),
    path('addReview/<name>', views.addReview, name='addReview'),
    # path('category/<int:id>', views.category, name='category'),
    # path('cart/', views.cart, name='cart'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('update_item/', views.updateItem, name='update_item'),
    # path('process_order/', views.processOrder, name='process_order'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)