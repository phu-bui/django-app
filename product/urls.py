from django.contrib import admin

from django.urls import path
from django.conf.urls import include
from .views import *


urlpatterns = [
    path('product/', ProductListView.as_view(), name = 'product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name = 'product_detail'),
    path('search/', search, name = 'search'),
    path('Computer&Laptop/', ComputersAndLaptopstListView.as_view(), name = 'computer&laptop'),
    path('Smartphone&Tablet/', SmartphonesAndTabletsListView.as_view(), name ='smartphone&tablet'),
    path('Camera&Photo/', CamerasAndPhotosListView.as_view(), name = 'camera&photo'),
    path('Hardware/', HardwareListView.as_view(), name = 'hardware'),
    path('TV&Audio/', TVAndAudioListView.as_view(), name = 'tv&audio'),
    path('Gadgets/', GadgetsListView.as_view(),name = 'gadget'),
    path('CarElectronic/', CarElectronicsListView.as_view(), name= 'carelectronic'),
    path('VideoGame&Console/', VideogamesAndConsolesListView.as_view(), name='videogame&console'),
    path('Accessori/', AccessoriesListView.as_view(), name='accessori'),
    path('Apple/', AppleBrandListView.as_view(), name = 'apple'),
    path('Sony/', SonyBrandListView.as_view(), name = 'sony'),
    path('Asus/', AsusBrandListView.as_view(), name = 'asus'),
    path('Dell/', DellBrandListView.as_view(), name = 'dell'),
    path('Blog/', PostListView.as_view(), name = 'blog'),
    path('Blog/<int:pk>', post, name = 'post'),
]
