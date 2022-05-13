from django.db import models

from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=256)


class Student(models.Model):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(default=20)
    gender = models.BooleanField(default=True, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=False, null=True)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})


class Course(models.Model):
    name = models.TextField(max_length=256)
    limit = models.IntegerField(default=30)
    startDate = models.DateField()
    endDate = models.DateField()
    students = models.ManyToManyField(Student, blank=True, null=True)

    def __str__(self):
        return f"{self.name}({self.id})"
