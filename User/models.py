from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=255)
    department_initial = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name + " ( " + self.department_initial + " )"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    roll = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15,default="N/A")

    def __str__(self):
        return self.user.get_full_name()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15,default="N/A")

    def __str__(self):
        return self.user.get_full_name()
