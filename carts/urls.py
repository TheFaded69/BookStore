from django.urls import path
from . import views

urlpatterns = [
    path('update/<str:book_id>/<int:delta>/', views.update_cart, name='update_cart'),
    path('', views.cart, name='cart_detail'),
]