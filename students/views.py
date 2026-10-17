from django.http import HttpResponse

def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>School Manager</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f4f8;
                margin: 0;
                text-align: center;
            }

            header {
                background-color: #17365d;
                color: white;
                padding: 30px;
            }

            h1 {
                margin: 0;
                font-size: 35px;
            }

            main {
                padding: 30px;
            }

            .carte {
                background-color: white;
                padding: 20px;
                margin: 15px auto;
                max-width: 450px;
                border-radius: 10px;
                box-shadow: 0 4px 8px #cccccc;
            }

            h2 {
                color: #17365d;
            }

            ul {
                list-style: none;
                padding: 0;
            }

            li {
                background-color: #e3ecf7;
                margin: 10px;
                padding: 12px;
                border-radius: 5px;
            }

            footer {
                background-color: #17365d;
                color: white;
                padding: 15px;
                margin-top: 30px;
            }
        </style>
    </head>

    <body>
        <header>
            <h1>School Manager</h1>
            <p>Votre plateforme de gestion scolaire</p>
        </header>

        <main>
            <div class="carte">
                <h2>Bienvenue !</h2>
                <p>Gérez facilement les informations de votre établissement scolaire.</p>
            </div>

            <div class="carte">
                <h2>Nos fonctionnalités</h2>

                <ul>
                    <li>Gestion des étudiants</li>
                    <li>Gestion des enseignants</li>
                    <li>Gestion des cours</li>
                    <li>Gestion des notes</li>
                </ul>
            </div>
        </main>

        <footer>
            <p>© 2026 School Manager - Gestion scolaire</p>
        </footer>
    </body>
    </html>
    """

    return HttpResponse(html)
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenue dans School Manager")


def student_list(request):
    return HttpResponse("Liste des étudiants")
def student_detail(request, id):
    return HttpResponse(f"Détail de l'étudiant {id}")

def teacher_list(request):
    return HttpResponse("Liste des enseignants")

def course_list(request):
    return HttpResponse("Liste des cours")

def about(request):
    return HttpResponse("À propos de School Manager")
