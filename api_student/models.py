from django.db import models

# Create your models here.


class Student(models.Model):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(default=20)
    gender = models.BooleanField(default=True, null=True, blank=True)
