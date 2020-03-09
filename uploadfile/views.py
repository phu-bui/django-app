from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from product.models import Category
import csv, io

@permission_required('admin.can_add_log_entry')
def category_upload(request):
    template = 'category_upload.html'
    prompt = {
        'order': 'Order of the CSV should be title, slug, description'
    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    date_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(date_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Category.objects.update_or_create(
            title=column[0],
            slug=column[1],
            description=column[2],
            active=column[3]
        )

    context = {}
    return render(request, template, context)