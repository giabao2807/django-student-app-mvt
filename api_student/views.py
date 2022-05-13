from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from api_student.forms import StudentForms, RawStudentForms
from api_student.models import Student


# def create_view(request):
#     form = RawStudentForms()
#
#     if request.method:
#         form = RawStudentForms(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Student.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#
#     context = {
#         'form': form
#     }
#     return render(request, 'create.html', context)

# def create_view(request):
#     if request.method =='post':
#         new_code = request.POST.get('code')
#         print(new_code)
#     context = {
#
#     }
#     return render(request, 'create.html', context)

def create_view(request):
    init_value = {
        'code': "102190252",
        'name': "Gia Bảo nè",
        'address': "Điện Bàn"
    }

    form = StudentForms(request.POST or None, initial=init_value)
    if form.is_valid():
        form.save()
        form = StudentForms()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def detail_view(request, id):
    # student = Student.objects.filter(id=id).first()
    student = get_object_or_404(Student, id=id)

    context = {
        'student': student
    }
    return render(request, 'detail.html', context)


def update_view(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForms(request.POST or None, instance=student)
    if request.method == 'POST':
        form.save()
        return redirect("/student")

    context = {
        'form': form
    }
    return render(request, 'update.html', context)


def delete_view(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect("/student")

    context = {
        'student': student
    }
    return render(request, 'delete.html', context)


def list_view(request):
    keyword = request.GET.get('keyword')
    if keyword:
        queryset = Student.objects.filter(name__icontains=keyword)
    else:
        queryset = Student.objects.all()
    context = {
        "keyword": keyword,
        'students': queryset
    }
    return render(request, 'list.html', context)