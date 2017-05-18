from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import StudentRegistrationForm, EditStudent
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        try:
            student = user.student.roll
            permission = False
        except ObjectDoesNotExist:
            permission = True
        if user is not None and permission:
            return JsonResponse({
                'success': True,
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'admin': user.is_superuser
                }
            })
        else:
            return JsonResponse({
                'success': False
            })
    else:
        return render(request, 'User/user-login.html')


@csrf_exempt
def add_student(request):
    if request.method == 'GET':
        form = StudentRegistrationForm()
        return render(request, 'User/register-student.html', {'form': form})
    elif request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        dept = request.POST.get('department')
        roll = request.POST.get('roll')
        phone_no = request.POST.get('phone_no')
        department = Department.objects.get(department_initial=dept)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            student = Student(user=user, department=department, roll=roll,phone_no=phone_no)
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
        phone_no = request.POST.get('phone_no')
        department = Department.objects.get(department_initial=dept)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            teacher = Teacher(user=user, department=department,phone_no=phone_no)
            teacher.save()
            return HttpResponse("Successfully Registered")
        else:
            return HttpResponse("Error occured with form")


@csrf_exempt
def all_teacher(request):
    teachers = Teacher.objects.all().order_by('-pk')
    response = []
    for item in teachers:
        response.append({
            'first_name': item.user.first_name,
            'last_name': item.user.last_name,
            'email': item.user.email,
            'username': item.user.username,
            'department': item.department.department_initial,
            'phone_no':item.phone_no
        })
    print(response)
    return JsonResponse(response, safe=False)


@csrf_exempt
def all_students(request):
    students = Student.objects.all().order_by('-pk')
    response = []
    for item in students:
        response.append({
            'first_name': item.user.first_name,
            'last_name': item.user.last_name,
            'email': item.user.email,
            'username': item.user.username,
            'department': item.department.department_initial,
            'roll': item.roll,
            'phone_no':item.phone_no
        })
    return JsonResponse(response, safe=False)


@csrf_exempt
def delete_student(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        User.objects.filter(username=username).delete()
        return HttpResponse("Deletion Successful")


@csrf_exempt
def edit_student(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = Department.objects.get(department_initial=request.POST.get("department"))
        roll = request.POST.get('roll')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        user_type = request.POST.get('user_type')
        user = User.objects.get(username=username)
        if user_type == 'student':
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            user.student.department = department
            user.student.roll = roll
            user.student.phone_no = phone_no
            user.student.save()
            return HttpResponse("Successfully Updated")
        else:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            user.teacher.department = department
            user.teacher.phone_no = phone_no
            user.teacher.save()
            return HttpResponse("Successfully Updated")
    else:
        form = EditStudent()
        return render(request, 'User/edit-teacher.html', {'form': form})
@csrf_exempt
def edit_student_new(request):
    return HttpResponse("Hello Edited Student")


@csrf_exempt
def edit_again(request):
    return HttpResponse("Edit Again")