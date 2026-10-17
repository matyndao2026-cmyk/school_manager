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

