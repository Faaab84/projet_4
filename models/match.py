from models.player import Joueur


class Match:
    # Initialise un match avec deux joueurs et leurs scores
    def __init__(self, joueur1, joueur2, scorej1=None, scorej2=None):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.scorej1 = scorej1
        self.scorej2 = scorej2

    # Enregistre les scores des deux joueurs pour le match
    def resultat(self, scorej1, scorej2):
        self.scorej1 = scorej1
        self.scorej2 = scorej2

    """Retourne une représentation par texte du match
    avec les noms des joueurs et leurs scores"""
    def __str__(self):
        score1 = self.scorej1 or "-"
        score2 = self.scorej2 or "-"
        return (f"{self.joueur1.prenom} {self.joueur1.nom} ({score1}) "
                f"vs {self.joueur2.prenom} {self.joueur2.nom} ({score2})")

    # Convertit les informations du match en un dictionnaire pour la sauvegarde
    def to_save(self):
        return {
            "joueur1": self.joueur1.to_save(),
            "joueur2": self.joueur2.to_save(),
            "scorej1": self.scorej1,
            "scorej2": self.scorej2
        }

    # Charge les informations d'un match à partir d'un dictionnaire
    def from_save(self, data):
        joueur1_data = data["joueur1"]
        joueur2_data = data["joueur2"]
        self.joueur1 = Joueur.from_save(joueur1_data)
        self.joueur2 = Joueur.from_save(joueur2_data)
        self.scorej1 = data.get("scorej1")
        self.scorej2 = data.get("scorej2")
