from django.urls import path
from django.conf.urls import include
from .views import *

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog123'),

]