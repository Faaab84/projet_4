import json
import os


class Joueur:
    # Initialise un joueur avec ses informations personnelles et son score
    def __init__(self, identifiant_national, prenom,
                 nom, date_de_naissance, score=0.0):
        self.identifiant_national = identifiant_national
        self.prenom = prenom
        self.nom = nom
        self.date_de_naissance = date_de_naissance
        self.score = score

    # Convertit les informations du joueur en dictionnaire pour sauvegarde
    def to_save(self):
        return {
            "identifiant_national": self.identifiant_national,
            "prenom": self.prenom,
            "nom": self.nom,
            "date_de_naissance": self.date_de_naissance,
            "score": self.score
        }

    # Crée une instance de Joueur à partir des données d'une sauvegarde
    @staticmethod
    def from_save(data):
        return Joueur(
            identifiant_national=data["identifiant_national"],
            prenom=data["prenom"],
            nom=data["nom"],
            date_de_naissance=data.get("date_de_naissance", ""),
            score=data.get("score", 0.0)
        )

    # Lit et retourne la liste des joueurs à partir d'un fichier JSON
    @staticmethod
    def read_json(fichier="joueurs.json"):
        if not os.path.exists(fichier):
            return []
        with open(fichier, "r", encoding="utf-8") as f:
            try:
                joueurs_data = json.load(f)
            except json.JSONDecodeError:
                return []
        joueurs = []
        for data in joueurs_data:
            joueur = Joueur.from_save(data)
            joueurs.append(joueur)
        return joueurs

    # Vérifie si un identifiant existe déjà dans le fichier des joueurs
    @staticmethod
    def id_existe(identifiant, fichier="joueurs.json"):
        joueurs = Joueur.read_json(fichier)
        for joueur in joueurs:
            if joueur.identifiant_national == identifiant:
                return True
        return False

    # Retourne un texte du joueur avec son nom, identifiant
    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.identifiant_national})"
