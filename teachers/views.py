from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Teacher
from .forms import TeacherForm


# LISTE DES ENSEIGNANTS
def teacher_list(request):
    teachers = Teacher.objects.all()

    context = {
        "teachers": teachers,
    }

    return render(request, "teachers/teacher_list.html", context)


# LISTE DES COURS
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


# INSCRIRE UN ENSEIGNANT
def teacher_create(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid():
            teacher = form.save()

            messages.success(
                request,
                f"L'enseignant {teacher} a été ajouté avec succès."
            )

            return redirect("teachers:teacher_list")

    else:
        form = TeacherForm()

    context = {
        "form": form,
        "title": "Ajouter un enseignant",
    }

    return render(request, "teachers/teacher_form.html", context)