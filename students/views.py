from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Student


# LISTE DES ETUDIANTS
def student_list(request):
    query = request.GET.get("q", "")

    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    context = {
        "students": students,
        "query": query,
    }

    return render(request, "students/student_list.html", context)


# DETAIL D'UN ETUDIANT
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    context = {
        "student": student,
    }

    return render(request, "students/student_detail.html", context)


# FILTRER LES ETUDIANTS PAR CLASSE
def students_by_class(request, classe):
    students = Student.objects.filter(classe=classe)

    context = {
        "students": students,
        "classe": classe,
    }

    return render(request, "students/student_list.html", context)