from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', next_page='/books/book_store/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/books/book_store/'), name='logout'),
]