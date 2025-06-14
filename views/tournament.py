

class TournamentCreation:
    """Collecte les informations et résultats pour les tournois d'échecs."""

    @staticmethod
    def demander_infos_tournoi():
        """Collecte le nombre de tours et la description du tournoi."""
        while True:
            TournamentCreation.display_prompt_round_count()
            nombre_tours = input().strip()
            if nombre_tours.lower() == "q":
                return None
            if nombre_tours == "":
                nombre_tours = 4
                break
            if nombre_tours.isdigit() and int(nombre_tours) > 0:
                nombre_tours = int(nombre_tours)
                break
            TournamentCreation.display_error_invalid_number()

        TournamentCreation.display_prompt_description()
        description = input().strip()
        if description.lower() == "q":
            return None

        return {
            "nombre_tours": nombre_tours,
            "description": description
        }

    @staticmethod
    def demander_resultat_match(match):
        """Collecte le résultat d'un match entre deux joueurs."""
        print(f"\nMatch: {match.joueur1.prenom} {match.joueur1.nom} "
              f"vs {match.joueur2.prenom} {match.joueur2.nom}")
        print(f"1. Victoire de {match.joueur1.prenom} {match.joueur1.nom}")
        print(f"2. Victoire de {match.joueur2.prenom} {match.joueur2.nom}")
        print("3. Match nul")
        while True:
            resultat = input("Résultat (1, 2, 3, ou 'q' pour quitter) : ").strip()
            if resultat.lower() == "q":
                return None
            if resultat in ["1", "2", "3"]:
                return resultat
            print("Choix invalide, veuillez entrer 1, 2, 3, ou 'q'.")

    @staticmethod
    def display_error_empty_name():
        """Affiche un message d'erreur pour un nom de tournoi vide."""
        print("Le nom du tournoi ne peut pas être vide.")

    @staticmethod
    def display_error_empty_location():
        """Affiche un message d'erreur pour un lieu de tournoi vide."""
        print("Le lieu ne peut pas être vide.")

    @staticmethod
    def display_error_insufficient_players():
        """Affiche un message d'erreur si moins de 2 joueurs sont disponibles."""
        print("Erreur : il faut au moins 2 joueurs pour créer un tournoi.")

    @staticmethod
    def display_available_players():
        """Affiche la liste des joueurs disponibles."""
        print("\nListe des joueurs disponibles :")

    @staticmethod
    def display_player(index, joueur):
        """Affiche un joueur avec son index."""
        print(f"{index}. {joueur.prenom} {joueur.nom}")

    @staticmethod
    def display_error_invalid_selection():
        """Affiche un message d'erreur pour une sélection de joueurs invalide."""
        print("Erreur : il faut sélectionner au moins 2 joueurs.")

    @staticmethod
    def display_tournament_created(tournoi, nombre_joueurs):
        """Affiche un message de confirmation de création du tournoi."""
        print(f"\nTournoi '{tournoi.nom}' créé avec {nombre_joueurs} "
              f"joueurs et {tournoi.nombre_tours} tours !")

    @staticmethod
    def display_round_title(round_name):
        """Affiche le titre d'un tour."""
        print(f"\n--- {round_name} ---")

    @staticmethod
    def display_no_valid_pairs():
        """Affiche un message si aucune paire de joueurs n'est possible."""
        print("Plus de matchs possibles, le tournoi est terminé !")

    @staticmethod
    def display_no_ongoing_tournaments():
        """Affiche un message s'il n'y a aucun tournoi en cours."""
        print("Aucun tournoi en cours à continuer.")

    @staticmethod
    def display_ongoing_tournaments():
        """Affiche l'en-tête de la liste des tournois en cours."""
        print("\nTournois en cours :")

    @staticmethod
    def display_tournament(index, tournoi):
        """Affiche un tournoi avec son index."""
        print(f"{index}. {tournoi.nom} ({tournoi.lieu}, {tournoi.date})")

    @staticmethod
    def display_error_invalid_tournament_number():
        """Affiche un message d'erreur pour un numéro de tournoi invalide."""
        print("Numéro invalide.")

    @staticmethod
    def display_error_invalid_input():
        """Affiche un message d'erreur pour une entrée non valide."""
        print("Entrée invalide.")

    @staticmethod
    def display_prompt_tournament_name():
        """Affiche l'invite pour saisir le nom du tournoi."""
        print("Nom du tournoi (ou 'q' pour quitter) : ", end="")

    @staticmethod
    def display_prompt_location():
        """Affiche l'invite pour saisir le lieu du tournoi."""
        print("Lieu du tournoi (ou 'q' pour quitter) : ", end="")

    @staticmethod
    def display_prompt_round_count():
        """Affiche l'invite pour saisir le nombre de tours."""
        print("Nombre de tours (par défaut 4, ou 'q' pour quitter) : ", end="")

    @staticmethod
    def display_prompt_description():
        """Affiche l'invite pour saisir la description du tournoi."""
        print("Description du tournoi (optionnel, ou 'q' pour quitter) : ", end="")

    @staticmethod
    def display_prompt_player_selection():
        """Affiche l'invite pour sélectionner les joueurs."""
        print("Numéros des joueurs à inscrire (séparés par des virgules, "
              "ou 'q' pour quitter) : ", end="")

    @staticmethod
    def display_prompt_tournament_selection():
        """Affiche l'invite pour sélectionner un tournoi en cours."""
        print("Numéro du tournoi à continuer (ou 'q' pour quitter) : ", end="")

    @staticmethod
    def display_error_invalid_number():
        """Affiche un message d'erreur pour un nombre invalide."""
        print("Veuillez entrer un nombre valide.")
