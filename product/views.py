from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import GetAllProductSerializers
from django.views.generic import ListView, DetailView
from itertools import chain
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from .forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
class GetAllProductAPIView(APIView):

    def get(self, request):
        list_product = Product.objects.all()
        mydate = GetAllProductSerializers(list_product, many = True)
        return Response(data = mydate.data, status = status.HTTP_200_OK)



from rest_framework import filters, generics
class ProductListView(ListView):
    queryset = Product.objects.all().order_by("-price")
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

class PostListView(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = 'product/blog.html'
    context_object_name = 'Post'
    paginate_by = 10

def post(request, pk):
    post = get_object_or_404(Post, pk = pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'product/post.html', {'post':post, 'form': form})

class ComputersAndLaptopstListView(ListView):
    queryset = Product.objects.filter(category__title='Computers And Laptops')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class CamerasAndPhotosListView(ListView):
    queryset = Product.objects.filter(category__title='Cameras And Photos')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class HardwareListView(ListView):
    queryset = Product.objects.filter(category__title='Hardware')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class SmartphonesAndTabletsListView(ListView):
    queryset = Product.objects.filter(category__title ='Smartphones And Tablets')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class TVAndAudioListView(ListView):
    queryset = Product.objects.filter(category__title='TV And Audio')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class GadgetsListView(ListView):
    queryset = Product.objects.filter(category__title='Gadgets')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class CarElectronicsListView(ListView):
    queryset = Product.objects.filter(category__title='Car Electronics')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class VideogamesAndConsolesListView(ListView):
    queryset = Product.objects.filter(category__title='Videogames And Consoles')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class AccessoriesListView(ListView):
    queryset = Product.objects.filter(category__title='Accessories')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class AppleBrandListView(ListView):
    queryset = Product.objects.filter(brand='Apple')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class SonyBrandListView(ListView):
    queryset = Product.objects.filter(brand='Sony')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class DellBrandListView(ListView):
    queryset = Product.objects.filter(brand='Dell')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10

class AsusBrandListView(ListView):
    queryset = Product.objects.filter(brand='Asus')
    template_name = 'product/product.html'
    context_object_name = 'Product'
    paginate_by = 10


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Product.objects.filter(Q(title__icontains=srch)|
                                           Q(category__title__icontains=srch))

            if match:
                return render(request, 'product/search.html', {'sr':match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request, 'product/search.html')
