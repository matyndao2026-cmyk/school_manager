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


