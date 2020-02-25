from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import GetAllProductSerializers
from django.views.generic import ListView
from itertools import chain
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

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

def product(request, pk):
    product = get_object_or_404(Product, pk = pk)
    return render(request, "product/product_detail.html", {"post": product})

class SearchView(ListView):
    template_name = 'search/view.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            blog_results = Product.objects.search(query)


            # combine querysets
            queryset_chain = chain(
                blog_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Product.objects.none()  # just an empty queryset as default
