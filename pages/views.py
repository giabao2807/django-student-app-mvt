from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request):
    context = {
        'name': 'Gia Bao',
        'skills': ['java', 'django'],
        'content': '<div class="alert alert-primary" role="alert">Hello Django!</div>'
    }
    return render(request, 'home.html', context)


def contact_view(request):
    return render(request, 'contact.html', {})


def about_view(request):
    return HttpResponse("<h1>About view</h1>")
