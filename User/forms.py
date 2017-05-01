from django import forms
from .models import *
from django.contrib.auth.models import User


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class EditStudent(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username']
