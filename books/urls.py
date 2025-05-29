from django.urls import path
from . import views

urlpatterns = [
    path('<str:book_id>', views.book, name='book'),
    path('book_store/', views.book_store, name='book_store'),
]