from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('upload-csv/', category_upload, name='category_upload'),
]

