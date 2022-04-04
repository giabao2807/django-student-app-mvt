from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request):
    return render(request, 'home.html', {'name': 'Gia Bao'})


def contact_view(request):
    return render(request, 'contact.html', {})


def about_view(request):
    return HttpResponse("<h1>About view</h1>")
