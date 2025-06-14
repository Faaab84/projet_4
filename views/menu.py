class Menu:
    """Gère l'affichage des menus et la collecte des choix de l'utilisateur."""

    @staticmethod
    def afficher_menu_principal():
        """Affiche le menu principal et récupère le choix."""
        print("\n============== Menu Principal ==============")
        print("1. Menu joueurs")
        print("2. Menu tournois")
        print("3. Rapports")
        print("4. Quitter")
        return input("Votre choix : ")

    @staticmethod
    def afficher_menu_joueur():
        """Affiche le menu des joueurs et récupère le choix."""
        print("\n============== Menu Joueur ==============")
        print("1. Créer un nouveau joueur")
        print("2. Afficher la liste des joueurs")
        print("3. Retour au menu principal")
        return input("Votre choix : ")

    @staticmethod
    def afficher_menu_tournois():
        """Affiche le menu des tournois et récupère le choix."""
        print("\n============== Menu Tournoi ==============")
        print("1. Démarrer un nouveau tournoi")
        print("2. Continuer un tournoi")
        print("3. Retour au menu principal")
        return input("Votre choix : ")
