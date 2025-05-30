class TournamentCreation:
    # Demande et valide les informations pour créer un tournoi
    @staticmethod
    def demander_infos_tournoi():
        while True:
            nombre_tours = input("Nombre de tours (par défaut 4, "
                                 "ou 'q' pour quitter) : ").strip()
            if nombre_tours.lower() == "q":
                return None
            if nombre_tours == "":
                nombre_tours = 4
                break
            if nombre_tours.isdigit() and int(nombre_tours) > 0:
                nombre_tours = int(nombre_tours)
                break
            print("Veuillez entrer un nombre valide.")

        description = input("Description du tournoi (optionnel,"
                            " ou 'q' pour quitter) : ").strip()
        if description.lower() == "q":
            return None

        return {
            "nombre_tours": nombre_tours,
            "description": description
        }

    # Demande et valide le résultat d'un match entre deux joueurs
    @staticmethod
    def demander_resultat_match(match):
        print(f"\nMatch: {match.joueur1.prenom} {match.joueur1.nom} "
              f"vs {match.joueur2.prenom} {match.joueur2.nom}")
        print(f"1. Victoire de {match.joueur1.prenom} {match.joueur1.nom}")
        print(f"2. Victoire de {match.joueur2.prenom} {match.joueur2.nom}")
        print("3. Match nul")
        while True:
            resultat = input("Résultat (1, 2, 3, ou"
                             " 'q' pour quitter) : ").strip()
            if resultat.lower() == "q":
                return None
            if resultat in ["1", "2", "3"]:
                return resultat
            print("Choix invalide, veuillez entrer 1, 2, 3, ou 'q'.")
