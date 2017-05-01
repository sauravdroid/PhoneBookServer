from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import StudentRegistrationForm
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate


# Create your views here.

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            return JsonResponse({
                'success': True,
                'user': {
                    'username': user.username,
                    'email': user.email
                }
            })
        else:
            return JsonResponse({
                'success': False
            })
    else:
        return render(request,'User/user-login.html')


@csrf_exempt
def add_student(request):
    if request.method == 'GET':
        form = StudentRegistrationForm()
        return render(request, 'User/register-student.html', {'form': form})
    elif request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        dept = request.POST.get('department')
        roll = request.POST.get('roll')
        department = Department.objects.get(department_initial=dept)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            student = Student(user=user, department=department, roll=roll)
            student.save()
            return HttpResponse("Successfully Registered")
        else:
            return HttpResponse("Error occured with form")


@csrf_exempt
def add_teacher(request):
    if request.method == 'GET':
        form = StudentRegistrationForm()
        return render(request, 'User/register-teacher.html', {'form': form})
    elif request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        dept = request.POST.get('department')
        department = Department.objects.get(department_initial=dept)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            teacher = Teacher(user=user, department=department)
            teacher.save()
            return HttpResponse("Successfully Registered")
        else:
            return HttpResponse("Error occured with form")


@csrf_exempt
def all_teacher(request):
    teachers = Teacher.objects.all()
    response = []
    for item in teachers:
        response.append({
            'first_name': item.user.first_name,
            'last_name': item.user.last_name,
            'email': item.user.email,
            'username': item.user.username,
            'department': item.department.department_initial
        })
    print(response)
    return JsonResponse(response, safe=False)


@csrf_exempt
def all_students(request):
    students = Student.objects.all()
    response = []
    for item in students:
        response.append({
            'first_name': item.user.first_name,
            'last_name': item.user.last_name,
            'email': item.user.email,
            'username': item.user.username,
            'department': item.department.department_initial,
            'roll': item.roll
        })
    return JsonResponse(response, safe=False)


@csrf_exempt
def delete_student(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        User.objects.filter(username=username).delete()
        return HttpResponse("Deletion Successful")
