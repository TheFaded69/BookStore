from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('remove/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('', views.carts, name='carts'),
]