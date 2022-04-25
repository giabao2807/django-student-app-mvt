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
