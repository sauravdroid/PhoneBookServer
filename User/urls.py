from django.conf.urls import url
from . import views

app_name = "user"
urlpatterns = [
    url(r'^add/student', views.add_student, name='add_student'),
    url(r'^add/teacher', views.add_teacher, name='add_teacher'),
    url(r'^all/teachers', views.all_teacher, name='all_teachers'),
    url(r'^all/students', views.all_students, name='all_students'),
    url(r'^delete/student', views.delete_student, name='delete_student'),
    url(r'^login', views.user_login, name='user_login'),
]
