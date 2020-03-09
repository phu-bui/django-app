from django.shortcuts import render
from itertools import chain
from django.views.generic import ListView
from product.models import Product
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q

def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Product.objects.filter(Q(title__icontains=srch))

            if match:
                return render(request, 'product/product_detail.html', {'sr':match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request, 'product/product_detail.html')
