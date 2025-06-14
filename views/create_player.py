from datetime import datetime
from models.player import Joueur


class Player_create:
    """Gère la création d'un joueur avec validation des informations."""

    @staticmethod
    def demander_infos_joueur():
        """Collecte et valide les informations pour créer un joueur."""
        Player_create.display_creation_header()

        while True:
            Player_create.display_prompt_last_name()
            nom = input().strip()
            if nom.lower() == 'q':
                return None
            if not nom:
                Player_create.display_error_empty_last_name()
                continue
            break

        while True:
            Player_create.display_prompt_first_name()
            prenom = input().strip()
            if prenom.lower() == 'q':
                return None
            if not prenom:
                Player_create.display_error_empty_first_name()
                continue
            break

        while True:
            Player_create.display_prompt_birth_date()
            date = input().strip()
            if date.lower() == 'q':
                return None
            try:
                datetime.strptime(date, "%d-%m-%Y")
                break
            except ValueError:
                Player_create.display_error_invalid_date_format()

        while True:
            Player_create.display_prompt_national_id()
            identifiant = input().upper().strip()
            if identifiant.lower() == 'q':
                return None
            if not (len(identifiant) == 7 and identifiant[:2].isalpha() and identifiant[2:].isdigit()):
                Player_create.display_error_invalid_id_format()
                continue
            if Joueur.id_existe(identifiant):
                Player_create.display_error_existing_id(identifiant)
                continue
            break

        return {
            "nom": nom,
            "prenom": prenom,
            "date_de_naissance": date,
            "identifiant_national": identifiant
        }

    @staticmethod
    def display_creation_header():
        """Affiche l'en-tête pour la création d'un joueur."""
        print("\n=== Création d'un nouveau joueur ===")

    @staticmethod
    def display_prompt_last_name():
        """Affiche l'invite pour saisir le nom."""
        print("Nom (ou 'q' pour quitter) : ", end="")

    @staticmethod
    def display_prompt_first_name():
        """Affiche l'invite pour saisir le prénom."""
        print("Prénom (ou 'q' pour quitter) : ", end="")

    @staticmethod
    def display_prompt_birth_date():
        """Affiche l'invite pour saisir la date de naissance."""
        print("Date de naissance (DD-MM-YYYY, ou 'q' pour quitter) : ", end="")

    @staticmethod
    def display_prompt_national_id():
        """Affiche l'invite pour saisir l'identifiant national."""
        print("Identifiant national (2 lettres + 5 chiffres, ou 'q' pour quitter) : ", end="")

    @staticmethod
    def display_error_empty_last_name():
        """Affiche un message d'erreur pour un nom vide."""
        print("Erreur : Le nom ne peut pas être vide")

    @staticmethod
    def display_error_empty_first_name():
        """Affiche un message d'erreur pour un prénom vide."""
        print("Erreur : Le prénom ne peut pas être vide")

    @staticmethod
    def display_error_invalid_date_format():
        """Affiche un message d'erreur pour un format de date invalide."""
        print("Format invalide ! Exemple : 21-05-1994")

    @staticmethod
    def display_error_invalid_id_format():
        """Affiche un message d'erreur pour un format d'identifiant invalide."""
        print("Format invalide ! Exemple : AB12345")

    @staticmethod
    def display_error_existing_id(identifiant):
        """Affiche un message d'erreur si l'identifiant existe déjà."""
        print(f"Erreur : L'ID {identifiant} existe déjà. Veuillez en saisir un autre.")

    @staticmethod
    def display_player_created(joueur):
        """Affiche un message de confirmation de création du joueur."""
        print(f"\nLe joueur {joueur.prenom} {joueur.nom} a été créé avec succès!")

    @staticmethod
    def display_no_players():
        """Affiche un message si aucun joueur n'est enregistré."""
        print("\nAucun joueur enregistré")

    @staticmethod
    def display_players_header():
        """Affiche l'en-tête de la liste des joueurs."""
        print("\n=== Liste des joueurs ===\n")

    @staticmethod
    def display_player(joueur):
        """Affiche un joueur."""
        print(joueur)
