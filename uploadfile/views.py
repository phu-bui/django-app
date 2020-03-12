from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from product.models import Category
import csv, io
@permission_required('admin.can_add_log_entry')
def category_upload(request):
    template = 'category_upload.html'
