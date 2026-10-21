from django.shortcuts import render
from django.http import Http404

# DONNEES DES ETUDIANTS

STUDENTS = [
{
"id": 1,
"first_name": "Awa",
"last_name": "Diop",
"classe": "L1",
"active": True,
},
{
"id": 2,
"first_name": "Fatou",
"last_name": "Ndiaye",
"classe": "L2",
"active": True,
},
{
"id": 3,
"first_name": "Moussa",
"last_name": "Fall",
"classe": "L1",
"active": False,
},
{
"id": 4,
"first_name": "Ibrahima",
"last_name": "Sow",
"classe": "L3",
"active": True,
},
]

# DONNEES DES ENSEIGNANTS

TEACHERS = [
{
"first_name": "Mamadou",
"last_name": "Ba",
"subject": "Mathématiques",
},
{
"first_name": "Aïssatou",
"last_name": "Sy",
"subject": "Informatique",
},
{
"first_name": "Cheikh",
"last_name": "Diallo",
"subject": "Anglais",
},
]

# PAGE D'ACCUEIL

def home(request):
    context = {
        "school_name": "Lycée d'Excellence de Dakar",
        "nb_classes": 12,
    }
    return render(request, "students/home.html", context)

# LISTE DES ETUDIANTS

def student_list(request):
    context = {
        "students": STUDENTS,
}
    return render(request, "students/student_list.html", context)

# DETAIL D'UN ETUDIANT

def student_detail(request, id):
    for student in STUDENTS:
        if student["id"] == id:
            return render(
                request,
                "students/student_detail.html",
                {"student": student},
            )

    raise Http404("Étudiant introuvable")


# LISTE DES ENSEIGNANTS


# LISTE DES ENSEIGNANTS

def teacher_list(request):
    context = {
        "teachers": TEACHERS,
    }
    return render(request, "students/teachers.html", context)
           

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

    return render(request, "students/courses.html", context)


# PAGE A PROPOS

def about(request):
    context = {
        "school_name": "Lycée d'Excellence de Dakar",
        "description": (
            "School Manager est une application de gestion scolaire "
            "permettant de consulter les étudiants, les enseignants "
            "et les cours de l'établissement."
        ),
    }
    return render(request, "students/about.html", context)

# FILTRER LES ETUDIANTS PAR CLASSE

def students_by_class(request, classe):
    students = []

    for student in STUDENTS:
        if student["classe"].upper() == classe.upper():
            students.append(student)

    context = {
        "students": students,
        "classe": classe,
    }

    return render(request, "students/student_list.html", context)
    def about(request): 
        return render(request, "students/about.html") 