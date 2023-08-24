from django.urls import path

from .views import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.products, name='products'),
    path('product/<int:id>', views.product, name='product'),
    # path('category/<int:id>', views.category, name='category'),
    # path('cart/', views.cart, name='cart'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('update_item/', views.updateItem, name='update_item'),
    # path('process_order/', views.processOrder, name='process_order'),
]