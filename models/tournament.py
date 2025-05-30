import json
import os
from datetime import datetime
from models.round import Round
from models.player import Joueur


class Tournois:
    # Initialise un tournoi avec ses informations de base et ses paramètres
    def __init__(self, nom, lieu, date, nombre_tours=4, description=""):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nombre_tours = nombre_tours
        self.description = description
        self.etat = "En cours"
        self.joueurs = []
        self.tours = []
        self.paires_jouees = []

    # Charge les données d'un tournoi à partir d'un dictionnaire
    def from_save(self, data):
        self.nom = data.get("nom", "")
        self.lieu = data.get("lieu", "")
        self.date = data.get("date", "")
        self.nombre_tours = data.get("nombre_tours", 4)
        self.description = data.get("description", "")
        self.etat = data.get("etat", "En cours")
        self.joueurs = []
        for j in data.get("joueurs", []):
            joueur = Joueur.from_save(j)
            self.joueurs.append(joueur)
        self.tours = []
        for t in data.get("tours", []):
            tour = Round("", [], "", "")
            tour.from_save(t)
            self.tours.append(tour)
        self.paires_jouees = []
        for p in data.get("paires_jouees", []):
            self.paires_jouees.append(p)

    # Charge une liste de tournois à partir d'un fichier JSON
    @classmethod
    def from_fichier(cls, fichier="tournois.json"):
        if not os.path.exists(fichier):
            return []
        with open(fichier, "r", encoding="utf-8") as f:
            try:
                liste_donnees = json.load(f)
            except json.JSONDecodeError:
                return []
        liste_tournois = []
        for data in liste_donnees:
            tournoi = cls("", "", "", 4, "")
            tournoi.from_save(data)
            liste_tournois.append(tournoi)
        return liste_tournois

    # Génère le premier tour du tournoi avec les joueurs inscrits
    def generer_premier_tour(self):
        nom_tour = "Tour 1"
        date_debut = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        date_fin = ""
        round1 = Round(nom_tour, self.joueurs, date_debut, date_fin)
        round1.generer_paire()
        self.tours = [round1]

    # Convertit les informations en dictionnaire pour la sauvegarde
    def to_save(self):
        return {
            "nom": self.nom,
            "lieu": self.lieu,
            "date": self.date,
            "nombre_tours": self.nombre_tours,
            "description": self.description,
            "etat": self.etat,
            "joueurs": [joueur.to_save() for joueur in self.joueurs],
            "tours": [tour.to_save() for tour in self.tours],
            "paires_jouees": self.paires_jouees
        }
