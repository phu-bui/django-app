from django.urls import path
from django.conf.urls import include
from .views import SearchView


urlpatterns = [
    path('search/', SearchView.as_view(), name = 'search'),

]
