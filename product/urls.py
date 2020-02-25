from django.contrib import admin

from django.urls import path
from django.conf.urls import include
from .views import SearchView, ProductListView, product


urlpatterns = [
    path('product/', ProductListView.as_view(), name = 'product'),
    path('<int:pk>/', product, name = 'product_detail')
]
