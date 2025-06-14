from datetime import datetime
from models.match import Match
from models.player import Joueur


class Round:
    """Représente un tour dans un tournoi d'échecs."""

    def __init__(self, nom="", joueurs=None, date_debut="", date_fin="", etat="Pas commencé"):
        """Initialise un tour avec ses informations."""
        self.nom = nom
        self.joueurs = joueurs if joueurs else []
        self.matchs = []
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.etat = etat

    def demarrer(self):
        """Démarre le tour en enregistrant la date de début."""
        if self.etat == "Pas commencé":
            self.date_debut = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.etat = "En cours"

    def terminer(self):
        """Termine le tour en enregistrant la date de fin."""
        if self.etat == "En cours":
            self.date_fin = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.etat = "Terminé"

    def generer_paire(self):
        """Génère des paires de joueurs pour les matchs du tour."""
        if len(self.joueurs) % 2 != 0:
            print(f"Le joueur {self.joueurs[-1]} n'a pas d'adversaire pour ce tour.")
            joueurs = self.joueurs[:-1]
        else:
            joueurs = self.joueurs

        for i in range(0, len(joueurs), 2):
            match = Match(joueurs[i], joueurs[i + 1])
            self.matchs.append(match)

    def afficher_matchs(self):
        """Affiche la liste des matchs du tour."""
        for idx, match in enumerate(self.matchs, 1):
            print(f"Match {idx}: {match}")

    def to_save(self):
        """Convertit le tour en dictionnaire pour la sauvegarde."""
        return {
            "nom": self.nom,
            "joueurs": [joueur.to_save() for joueur in self.joueurs],
            "matchs": [match.to_save() for match in self.matchs],
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "etat": self.etat
        }

    def from_save(self, data):
        """Charge les informations d'un tour à partir d'un dictionnaire."""
        self.nom = data.get("nom", "")
        self.joueurs = []
        for j in data.get("joueurs", []):
            joueur = Joueur.from_save(j)
            self.joueurs.append(joueur)
        self.matchs = []
        for m in data.get("matchs", []):
            match = Match(None, None)
            match.from_save(m)
            self.matchs.append(match)
        self.date_debut = data.get("date_debut", "")
        self.date_fin = data.get("date_fin", "")
        self.etat = data.get("etat", "Pas commencé")
