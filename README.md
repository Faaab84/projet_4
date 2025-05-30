# OpenClassrooms: Projet 4: Chess Tournament
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
- Le programme vous permet de gérer des tournois d'échecs. Lors de la première utilisation, sélectionnez "Créer un tournoi", puis laissez vous guider.
- Si aucun joueurs n'est présent dans la base de donnée, vous serez invité à en créer.
- Lors d'un tournoi, vous serez invité à rentrer les résultats après chaque match. A la fin d'un tournoi, un classement sera généré.
- Pendant le tournoi, vous aurez la possibilité de sauvegarder le tournoi en cours, en charger un nouveau, de voir ou modifier les classements.
### 2) Menu tournois
- Cette section vous permet de charger un tournoi depuis la base de donnée.
- Une fois le tournoi chargé, vous serez invité à le continuer.
### 3) Menu Rapports
- Lorsque vous sélectionnez cette option, vous êtes invité à rentrer le nombre de joueurs à créer.
- Laissez vous ensuite guider par le programme.

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
