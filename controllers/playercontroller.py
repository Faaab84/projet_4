
from models.player import Joueur
from views.create_player import Player_create


class JoueurController:

    def __init__(self):  # initialisation du constructeur de la classe
        self.vue = Player_create()

    def creer_joueur(self):  # méthode pour créer un nouveau joueur
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
        Joueur.save_joueur(joueur)
        print(f"\nLe joueur {joueur.prenom} {joueur.nom} a été créé "
              f"avec succès!")
        return joueur

    def lister_joueurs(self):
        joueurs = Joueur.read_json()
        if not joueurs:
            print("\nAucun joueur enregistré")
            return
        joueurs.sort(key=lambda joueur: joueur.nom.lower())
        print("\n=== Liste des joueurs ===\n")
        for joueur in joueurs:
            print(joueur)

