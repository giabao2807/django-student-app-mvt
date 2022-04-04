from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from api_student.models import Student


def detail_view(request):
    student = Student.objects.filter(id=1).first()
    context = {
        'student': student
    }
    return render(request, 'detail.html', context)
