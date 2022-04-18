from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from api_student.forms import StudentForms
from api_student.models import Student

def create_view(request):
    if request.method =='post':
        new_code = request.POST.get('code')
        print(new_code)
    context = {

    }
    return render(request, 'create.html', context)

# def create_view(request):
#     form = StudentForms
#     if form.is_valid():
#         form.save()
#     context = {
#         'form': form
#     }
#     return render(request, 'create.html', context)

def detail_view(request):
    student = Student.objects.filter(id=1).first()
    context = {
        'student': student
    }
    return render(request, 'detail.html', context)
