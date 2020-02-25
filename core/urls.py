from django.contrib import admin
from django.urls import path
from .views import HomeView
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', HomeView.as_view(), name = 'index'),
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name= 'homepage/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = '/'), name = 'logout'),
]
