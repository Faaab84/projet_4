from models.match import Match
from models.player import Joueur
from datetime import datetime


class Round:
    """ Initialise un round avec un nom,
    une liste de joueurs, des dates et un état"""
    def __init__(self, nom="", joueurs=None, date_debut="",
                 date_fin="", etat="Pas commencé"):
        self.nom = nom
        self.joueurs = joueurs if joueurs else []
        self.matchs = []
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.etat = etat

    # Démarre le round avec la date de début et en mettant à jour l'état
    def demarrer(self):
        if self.etat == "Pas commencé":
            self.date_debut = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.etat = "En cours"

    # Termine le round avec la date de fin et en mettant à jour l'état
    def terminer(self):
        if self.etat == "En cours":
            self.date_fin = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.etat = "Terminé"

    # Génère des paires de joueurs pour les matchs du round
    def generer_paire(self):
        if len(self.joueurs) % 2 != 0:
            print(f"Le joueur {self.joueurs[-1]} "
                  f"n'a pas d'adversaire pour ce tour.")
            joueurs = self.joueurs[:-1]
        else:
            joueurs = self.joueurs

        for i in range(0, len(joueurs), 2):
            match = Match(joueurs[i], joueurs[i + 1])
            self.matchs.append(match)

    # Affiche la liste des matchs du round
    def afficher_matchs(self):
        for idx, match in enumerate(self.matchs, 1):
            print(f"Match {idx}: {match}")

    # Convertit les informations du round en un dictionnaire pour la sauvegarde
    def to_save(self):
        return {
            "nom": self.nom,
            "joueurs": [joueur.to_save() for joueur in self.joueurs],
            "matchs": [match.to_save() for match in self.matchs],
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "etat": self.etat
        }

    # Charge les informations d'un round à partir d'un dictionnaire
    def from_save(self, data):
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
