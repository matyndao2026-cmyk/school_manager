
from django.contrib import admin
from django.urls import path

from students.views import (
    home,
    student_list,
    student_detail,
    teacher_list,
    course_list,
    about,
    students_by_class,
)

urlpatterns = [
    # Administration
    path('admin/', admin.site.urls),

    # Page d'accueil
    path('', home, name='home'),

    # Étudiants
    path('students/', student_list, name='student_list'),
    path(
        'students/classe/<str:classe>/',
        students_by_class,
        name='students_by_class',
    ),
    path(
        'students/<int:id>/',
        student_detail,
        name='student_detail',
    ),

    # Enseignants
    path('teachers/', teacher_list, name='teacher_list'),

    # Cours
    path('courses/', course_list, name='course_list'),

    # À propos
    path('about/', about, name='about'),
]

