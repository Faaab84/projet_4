import json
import os


class Joueur:
    """Représente un joueur dans un tournoi d'échecs."""

    def __init__(self, identifiant_national, prenom, nom, date_de_naissance, score=0.0):
        """Initialise un joueur avec ses informations."""
        self.identifiant_national = identifiant_national
        self.prenom = prenom
        self.nom = nom
        self.date_de_naissance = date_de_naissance
        self.score = score

    def to_save(self):
        """Convertit le joueur en dictionnaire pour la sauvegarde."""
        return {
            "identifiant_national": self.identifiant_national,
            "prenom": self.prenom,
            "nom": self.nom,
            "date_de_naissance": self.date_de_naissance,
            "score": self.score
        }

    @staticmethod
    def from_save(data):
        """Crée un joueur à partir d'un dictionnaire."""
        return Joueur(
            identifiant_national=data["identifiant_national"],
            prenom=data["prenom"],
            nom=data["nom"],
            date_de_naissance=data.get("date_de_naissance", ""),
            score=data.get("score", 0.0)
        )

    @staticmethod
    def read_json(fichier="joueurs.json"):
        """Lit la liste des joueurs depuis un fichier JSON."""
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

    @staticmethod
    def id_existe(identifiant, fichier="joueurs.json"):
        """Vérifie si un identifiant de joueur existe dans le fichier JSON."""
        joueurs = Joueur.read_json(fichier)
        for joueur in joueurs:
            if joueur.identifiant_national == identifiant:
                return True
        return False

    @staticmethod
    def save_joueur(joueur, fichier="joueurs.json"):
        """Enregistre un joueur dans un fichier JSON."""
        if os.path.exists(fichier):
            with open(fichier, "r", encoding="utf-8") as f:
                try:
                    joueurs_data = json.load(f)
                except json.JSONDecodeError:
                    joueurs_data = []
        else:
            joueurs_data = []
        joueurs_data.append(joueur.to_save())
        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(joueurs_data, f, ensure_ascii=False, indent=4)

    def __str__(self):
        """Retourne une représentation textuelle du joueur."""
        return f"{self.nom} {self.prenom} ({self.identifiant_national})"
