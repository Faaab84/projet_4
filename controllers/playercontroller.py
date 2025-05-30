from models.player import Joueur
from views.create_player import Player_create
import json
import os


class JoueurController:
    def __init__(self):
        self.vue = Player_create()

    def creer_joueur(self):

        infos = self.vue.demander_infos_joueur()

        if infos is None:
            return None

        joueur = Joueur(
            identifiant_national=infos["identifiant_national"],
            prenom=infos["prenom"],
            nom=infos["nom"],
            date_de_naissance=infos["date_de_naissance"],
            score=0.0
        )

        self.sauvegarder_joueur(joueur)
        print(f"\nLe joueur {joueur.prenom} {joueur.nom} a été "
              f"créé avec succès!")
        return joueur

    def sauvegarder_joueur(self, joueur, fichier="joueurs.json"):
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

    def lister_joueurs(self):
        joueurs = Joueur.read_json()

        if not joueurs:
            print("\nAucun joueur enregistré")
            return

        print("\n=== Liste des joueurs ===\n")
        for joueur in joueurs:
            print(joueur)
