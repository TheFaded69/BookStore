from django.urls import path
from . import views

urlpatterns = [
    path('<int:book_id>', views.book, name='book_detail'),
    path('book_store/', views.book_store, name='book_store'),
]