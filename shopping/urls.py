from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('product.urls')),
    path('', include('search.urls')),
    path('', include('uploadfile.urls'))
]

