from models.player import Joueur


class Match:
    """Représente un match entre deux joueurs dans un tournoi d'échecs."""

    def __init__(self, joueur1, joueur2, scorej1=None, scorej2=None):
        """Initialise un match avec deux joueurs et leurs scores."""
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.scorej1 = scorej1
        self.scorej2 = scorej2

    def resultat(self, scorej1, scorej2):
        """Enregistre les scores des joueurs pour le match."""
        self.scorej1 = scorej1
        self.scorej2 = scorej2

    def __str__(self):
        """Retourne une représentation textuelle du match."""
        score1 = self.scorej1 or "-"
        score2 = self.scorej2 or "-"
        return (f"{self.joueur1.prenom} {self.joueur1.nom} ({score1}) "
                f"vs {self.joueur2.prenom} {self.joueur2.nom} ({score2})")

    def to_save(self):
        """Convertit le match en dictionnaire pour la sauvegarde."""
        return {
            "joueur1": self.joueur1.to_save(),
            "joueur2": self.joueur2.to_save(),
            "scorej1": self.scorej1,
            "scorej2": self.scorej2
        }

    def from_save(self, data):
        """Charge les informations d'un match depuis un dictionnaire."""
        joueur1_data = data["joueur1"]
        joueur2_data = data["joueur2"]
        self.joueur1 = Joueur.from_save(joueur1_data)
        self.joueur2 = Joueur.from_save(joueur2_data)
        self.scorej1 = data.get("scorej1")
        self.scorej2 = data.get("scorej2")
