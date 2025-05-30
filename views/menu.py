class Menu:
    @staticmethod
    # Affiche le menu et récupère le choix de l'utilisateur
    def afficher_menu_principal():
        print("\n============== Menu Principal ==============")
        print("1. Menu joueurs")
        print("2. Menu tournois")
        print("3. Rapports")
        print("4. Quitter")
        return input("Votre choix : ")

    @staticmethod
    # Affiche le menu des joueurs et récupère le choix
    def afficher_menu_joueur():
        print("\n============== Menu Joueur ==============")
        print("1. Créer un nouveau joueur")
        print("2. Afficher la liste des joueurs")
        print("3. Retour au menu principal")
        return input("Votre choix : ")

    @staticmethod
    # Affiche le menu des options et récupère le choix
    def afficher_menu_tournois():
        print("\n============== Menu Tournoi ==============")
        print("1. Démarrer un nouveau tournoi")
        print("2. Continuer un tournoi")
        print("3. Retour au menu principal")
        return input("Votre choix : ")
