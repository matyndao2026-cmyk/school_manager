from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Student
from .forms import StudentForm


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


# INSCRIRE UN ETUDIANT
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save()

            messages.success(
                request,
                f"{student} a été inscrit(e)."
            )

            return redirect("students:student_detail", id=student.id)

    else:
        form = StudentForm()

    context = {
        "form": form,
        "title": "Inscrire un étudiant"
    }

    return render(request, "students/student_form.html", context)


# MODIFIER UN ETUDIANT
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                f"La fiche de {student} a été mise à jour."
            )

            return redirect("students:student_detail", id=student.id)

    else:
        form = StudentForm(instance=student)

    context = {
        "form": form,
        "title": f"Modifier {student}",
        "student": student,
    }

    return render(request, "students/student_form.html", context)


# SUPPRIMER UN ETUDIANT
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        name = str(student)
        student.delete()

        messages.success(
            request,
            f"{name} a été supprimé(e)."
        )

        return redirect("students:student_list")

    context = {
        "student": student,
    }

    return render(
        request,
        "students/student_confirm_delete.html",
        context
    )