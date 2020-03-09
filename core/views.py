from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForms

# Create your views here.
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')

def contact(request):
    return render(request, 'homepage/contact.html')

def register(request):
    form = RegistrationForms()
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(request, 'homepage/register.html', {'form' : form})
