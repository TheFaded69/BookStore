from django.urls import path
from . import views

urlpatterns = [
    path('book_store/',views.BookStoreView.as_view(), name='book_store'),
    path('<str:book_id>/', views.BookDetailView.as_view(), name='book_detail'),
]