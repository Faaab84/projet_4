from models.player import Joueur
from views.create_player import Player_create


class JoueurController:
    """Gère les opérations liées aux joueurs dans le tournoi."""

    def __init__(self):
        """Initialise le contrôleur avec une vue pour la création de joueurs."""
        self.vue = Player_create()

    def creer_joueur(self):
        """Crée un nouveau joueur à partir des informations utilisateur."""
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
        self.vue.display_player_created(joueur)
        return joueur

    def lister_joueurs(self):
        """Affiche la liste des joueurs triée par nom."""
        joueurs = Joueur.read_json()
        if not joueurs:
            self.vue.display_no_players()
            return
        joueurs.sort(key=lambda joueur: joueur.nom.lower())
        self.vue.display_players_header()
        for joueur in joueurs:
            self.vue.display_player(joueur)
