# School Manager

## 1. Description du projet

School Manager est une application web développée avec Django. Elle permet de présenter différentes sections d'une application de gestion scolaire.

## 2. Prérequis

Avant de commencer, il faut installer :

* Python
* pip, pour installer les bibliothèques Python
* Un éditeur de code, comme Visual Studio Code
* Git, pour gérer les versions du projet

## 3. Installation du projet

### Étape 1 : Créer et activer l'environnement virtuel

Créer l'environnement virtuel :


python -m venv venv


Activer l'environnement virtuel sous Windows :


venv\Scripts\activate


### Étape 2 : Installer Django

Installer Django :


python -m pip install Django


Ou installer les dépendances du projet :


python -m pip install -r requirements.txt


### Étape 3 : Appliquer les migrations


python manage.py migrate


### Étape 4 : Lancer le serveur


python manage.py runserver


### Étape 5 : Accéder au site

Ouvrir le navigateur et saisir :

http://127.0.0.1:8000/

## 4. Fonctionnalités

* Page d'accueil avec les liens de navigation
* Liste des étudiants
* Détail d'un étudiant selon son identifiant
* Liste des enseignants
* Liste des cours
* Page À propos

## 5. Technologies utilisées

* Python
* Django
* Git
* HTML

## 6. Adresses des pages

* Accueil : `/`
* Étudiants : `/students/`
* Détail d'un étudiant : `/students/15/`
* Enseignants : `/teachers/`
* Cours : `/courses/`
* À propos : `/about/`
* Administration Django : `/admin/`

## 7. Questions de compréhension

### 1. Pourquoi utilise-t-on un environnement virtuel ?

Un environnement virtuel permet d'isoler les bibliothèques d'un projet Python de celles des autres projets. Cela évite les conflits entre les différentes versions des bibliothèques.

### 2. Pourquoi Django a-t-il besoin de Python ?

Django est un framework développé en Python. Il utilise donc Python pour exécuter le code de l'application web.

### 3. Quelle est la différence entre un projet Django et une application Django ?

Un projet Django représente l'ensemble du site web et sa configuration. Une application Django est une partie du projet qui remplit une fonction précise, par exemple gérer les étudiants.

### 4. À quoi sert le fichier `urls.py` ?

Le fichier `urls.py` définit les adresses URL du site et indique quelle vue doit être appelée pour chaque adresse.

### 5. À quoi sert le fichier `views.py` ?

Le fichier `views.py` contient les fonctions ou les classes qui traitent les requêtes des utilisateurs et préparent les réponses à renvoyer au navigateur.

### 6. Que se passe-t-il lorsque le navigateur demande `/students/` ?

Django reçoit la requête, recherche l'URL `/students/` dans `urls.py`, puis appelle la vue associée. Cette vue prépare et renvoie une réponse au navigateur.

### 7. Pourquoi utilise-t-on Git ?

Git permet de suivre les modifications du code, de conserver l'historique du projet et de revenir à une version précédente si nécessaire.


# 23. Validation individuelle

## 1. Quelle est la différence entre `HttpResponse` et `render()` ?

`HttpResponse` permet de renvoyer directement une réponse au navigateur, par exemple du texte ou du code HTML.

`render()` permet d'afficher une page HTML à partir d'un template Django. Il peut également transmettre des données à cette page.

## 2. Quels sont les trois arguments de `render()` ?

La fonction `render()` utilise principalement trois arguments :

* `request` : représente la requête envoyée par le navigateur.
* Le nom du template : indique le fichier HTML à afficher.
* `context` : un dictionnaire qui contient les données à transmettre au template.

Exemple :

```python
return render(request, "students/student_list.html", context)
```

## 3. Pourquoi placer les templates dans `students/templates/students/` ?

Cette organisation permet de séparer les templates de chaque application Django.

Le premier dossier `templates` contient les fichiers HTML. Le deuxième dossier `students` permet d'identifier les templates appartenant à l'application `students`.

Cela réduit également les risques de conflits lorsque plusieurs applications possèdent des templates portant le même nom.

## 4. Quelle est la différence entre `{{ ... }}` et `{% ... %}` ?

* `{{ ... }}` permet d'afficher une valeur dans une page HTML.

Exemple :

```django
{{ student.first_name }}
```

* `{% ... %}` permet d'exécuter une instruction du système de templates Django, comme une boucle, une condition ou l'héritage d'un template.

Exemple :

```django
{% for student in students %}
    <p>{{ student.first_name }}</p>
{% endfor %}
```

## 5. Pourquoi utiliser `{% url 'student_list' %}` plutôt que `/students/` ?

`{% url 'student_list' %}` permet à Django de générer automatiquement l'adresse associée au nom de route `student_list`.

Cette méthode est préférable, car si l'adresse de la page change dans `urls.py`, Django peut générer la nouvelle adresse sans qu'il soit nécessaire de modifier tous les liens des templates.

Exemple :

```django
<a href="{% url 'student_list' %}">Liste des étudiants</a>
```

## 6. À quoi servent `{% extends %}` et `{% block %}` ?

`{% extends %}` permet à un template de réutiliser la structure d'un autre template.

`{% block %}` définit une partie de la page qui peut être personnalisée dans un template enfant.

Exemple dans `base.html` :

```django
{% block content %}
{% endblock %}
```

Exemple dans `students/home.html` :

```django
{% extends "base.html" %}

{% block content %}
    <h1>Bienvenue sur School Manager</h1>
{% endblock %}
```

Cette organisation permet de partager la même structure, notamment le menu de navigation, entre plusieurs pages.

## 7. Pourquoi éviter de mettre le HTML directement dans les vues ?

Les vues doivent principalement gérer le traitement des requêtes et la préparation des données.

Les templates doivent gérer la présentation HTML.

Séparer ces responsabilités rend le code plus lisible, plus facile à maintenir et plus simple à modifier.

---

# 24. Et la suite ? — Perspectives d'amélioration

Actuellement, les étudiants sont stockés dans une liste Python appelée `STUDENTS` dans le fichier `students/views.py`.

Cette solution convient pour apprendre Django, mais elle présente plusieurs limites :

* Les données ne sont pas conservées durablement dans une base de données.
* L'ajout ou la modification d'un étudiant nécessite actuellement de modifier le code.
* La gestion d'un grand nombre d'étudiants devient difficile.

Pour améliorer l'application, les prochaines étapes seront :

1. **Les modèles Django (`Models`)** : définir la structure des données des étudiants.
2. **La base de données** : enregistrer durablement les étudiants.
3. **Les migrations** : créer et mettre à jour les tables de la base de données.
4. **L'ORM Django** : consulter et manipuler les données avec Python.
5. **Les fonctionnalités CRUD** : ajouter, afficher, modifier et supprimer des étudiants.
6. **La recherche** : permettre de retrouver facilement un étudiant.

Par exemple, une vue pourra ensuite récupérer les étudiants depuis la base de données :

```python
students = Student.objects.all()
```

Les données seront alors récupérées depuis le modèle `Student`, au lieu d'être directement stockées dans une liste Python.

## Conclusion

Ce TP m'a permis de découvrir les vues Django, les URL, les templates HTML, le passage de données aux pages, les conditions, les boucles et l'héritage des templates.

J'ai également appris à organiser une application Django en séparant le traitement des requêtes de la présentation des pages.

La prochaine étape sera de connecter l'application à une base de données afin de rendre la gestion des étudiants plus complète et professionnelle.
