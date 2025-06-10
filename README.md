# OpenClassrooms: Projet 4: 
Ce programme a été créé dans le cadre du projet 4 d'OpenClassrooms. Il s'agit d'un gestionnaire de tournois d'échecs.
## Installation:
Commencez tout d'abord par installer Python.
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/Faaab84/projet_4.git
```
Placez vous dans le dossier , puis creer et demarrer l'environnement virtuel:
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

### 1) Menu joueurs
- Le menu joueurs vous permets de créer un joueur avec un nom, prenom, date de naissance, et un identifiant unique.
- Vous pouvez egalement afficher la liste des joueurs.

### 2) Menu tournois
- Le menu tournoi vous permets de démarrer un nouveau tournoi avec : (un nom de tournoi, un lieu du tournoi,un nombre de tour, description)
- Il faut au minimum 2 joueurs inscrit dans l'application pour pouvoir selectionner les joueurs pour le tournoi à demarrer.
- Une fois le tournoi demarrer des paires vont être generer,les joueurs seront dans un premier temps trié aleoiterement et ne se rencontrerons jamais deux fois durant le tournoi.
- Pour chaque match vous serez invité à indiqué le joueur gagnant ou si il y a egalité.
- Une fois que les matchs/tours sont terminés ou si les joueurs ont tous eu un adversaire unique.Le tournoi prend fin.
- Un classement du tournoi sera afficher par ordre decroissant de points ainsi que les resultats des matchs du tournoi.
- Le match etant terminé vous pouvez le consulter par le menu Rapport en selectionnant le bon nom du tournoi.
- Vous pouvez egalement à tout moment revenir au menu principale et/ou quitter l'application puis continuer un tournoi deja en cours.
 
### 3) Menu Rapports
- Lorsque vous sélectionnez cette option, vous pouvez consulter un tournoi terminez afin de voir le classement et les resultats des matchs lors des differend tours.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Rapport Flake8

 activez l'environnement virtuel.
```
env\Scripts\activate
```
puis faites la commande
```
flake8 --format=html --htmldir=flake-report
```
- Le rapport sera généré dans le dossier flake-report.
