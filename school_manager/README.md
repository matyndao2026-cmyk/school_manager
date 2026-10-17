# School Manager

## Description

School Manager est un projet web développé avec Django. Il permet de présenter différentes sections d'une application de gestion scolaire.

## Fonctionnalités

* Page d'accueil
* Liste des étudiants
* Détail d'un étudiant selon son identifiant
* Liste des enseignants
* Liste des cours
* Page À propos

## Technologies utilisées

* Python
* Django
* Git

## Installation

1. Installer Python.

2. Installer les dépendances avec la commande :

   `python -m pip install -r requirements.txt`

3. Appliquer les migrations :

   `python manage.py migrate`

4. Lancer le serveur :

   `python manage.py runserver`

5. Ouvrir le navigateur à l'adresse `http://127.0.0.1:8000/`.

## Adresses des pages

* Accueil : `/`
* Étudiants : `/students/`
* Détail d'un étudiant : `/students/15/`
* Enseignants : `/teachers/`
* Cours : `/courses/`
* À propos : `/about/`
