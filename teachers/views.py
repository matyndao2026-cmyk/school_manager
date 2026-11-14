from django.shortcuts import render
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()

    context = {
        "teachers": teachers,
    }

    return render(request, "teachers/teacher_list.html", context)


def course_list(request):
    courses = [
        {"nom": "Mathématiques", "classe": "L1"},
        {"nom": "Informatique", "classe": "L2"},
        {"nom": "Français", "classe": "L1"},
    ]

    context = {
        "courses": courses,
    }

    return render(request, "teachers/course_list.html", context)