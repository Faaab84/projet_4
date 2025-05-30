# OpenClassrooms: Projet 4: 
Ce programme a été créé dans le cadre du projet 4 d'OpenClassrooms. Il s'agit d'un gestionnaire de tournois d'échecs.
## Installation:
Commencez tout d'abord par installer Python.
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/Faaab84/projet_4.git
```
Placez vous dans le dossier projet_4-main/projet_4-main, puis creer et demarrer l'environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
```
env\Scripts\activate
```
Il ne reste plus qu'à installer les packages requis:
```
pip install -r requirements.txt
```
Vous pouvez enfin lancer le script:
```
python main.py
```

## Utilisation
Le menu principal est divisé en 3 options.

### 1) Menu joueurs
- Le menu joueurs vous permets de créer un joueur avec un nom, prenom, date de naissance, et un identifiant unique.
- Vous pouvez egalement afficher la liste des joueurs.
- 
### 2) Menu Tournois
Le menu Tournois vous permet de démarrer un nouveau tournoi avec : un nom de tournoi, un lieu du tournoi, un nombre de tours, une description.

- Il faut au minimum 2 joueurs inscrits dans l'application pour pouvoir sélectionner les joueurs pour le tournoi à démarrer.
- Une fois le tournoi démarré, des paires vont être générées. Les joueurs seront dans un premier temps triés aléatoirement et ne se rencontreront jamais deux fois durant le tournoi.

- Pour chaque match, vous serez invité à indiquer le joueur gagnant ou s'il y a égalité.

-Une fois que les matchs/tours sont terminés ou si les joueurs ont tous eu un adversaire unique, le tournoi prend fin.

- Un classement du tournoi sera affiché par ordre décroissant de points, ainsi que les résultats des matchs du tournoi.

-Le match étant terminé, vous pouvez le consulter par le menu Rapport en sélectionnant le bon nom du tournoi.
Vous pouvez également à tout moment revenir au menu principal et/ou quitter l'application puis continuer un tournoi déjà en cours.

### 3) Menu Rapports
-Le menu Rapports vous permet de consulter un tournoi terminé. Vous pouvez voir les résultats pour chaque match et le classement.
Generer le rapport Flake 8
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- Installez flake8 avec la commande: 
```
pip intall flake8-html
```
- S'il n'existe pas, créer un fichier setup.cfg
- Ecrire le texte suivant dedans:
```
[flake8]
exclude = .git, env, __pycache__, .gitignore
max-line-length = 119
```
- Tapez la commande:
```
flake8 --format=html --htmldir=flake-report
```
- Le rapport sera généré dans le dossier flake8.
