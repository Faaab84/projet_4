from datetime import datetime
from models.player import Joueur


class Player_create:
    """ Demander les infos pour creer le joueur et
    on verifie que l'id n'existe pas"""
    @staticmethod
    def demander_infos_joueur():
        print("\n=== Création d'un nouveau joueur ===")

        while True:
            nom = input("Nom (ou 'q' pour quitter) : ").strip()
            if nom.lower() == 'q':
                return None
            if not nom:
                print("Erreur : Le nom ne peut pas être vide")
                continue
            break

        while True:
            prenom = input("Prénom (ou 'q' pour quitter) : ").strip()
            if prenom.lower() == 'q':
                return None
            if not prenom:
                print("Erreur : Le prénom ne peut pas être vide")
                continue
            break

        while True:
            date = input("Date de naissance (DD-MM-YYYY,"
                         " ou 'q' pour quitter) : ").strip()
            if date.lower() == 'q':
                return None
            try:
                datetime.strptime(date, "%d-%m-%Y")
                break
            except ValueError:
                print("Format invalide ! Exemple : 21-05-1994")

        while True:
            identifiant = input("Identifiant national (2 lettres +"
                                " 5 chiffres, ou 'q' pour quitter) :"
                                " ").upper().strip()
            if identifiant.lower() == 'q':
                return None
            if not (len(identifiant) == 7 and identifiant[:2].isalpha()
                    and identifiant[2:].isdigit()):
                print("Format invalide ! Exemple : AB12345")
                continue
            if Joueur.id_existe(identifiant):
                print(f"Erreur : L'ID {identifiant} existe déjà."
                      f" Veuillez en saisir un autre.")
                continue
            break

        return {
            "nom": nom,
            "prenom": prenom,
            "date_de_naissance": date,
            "identifiant_national": identifiant
        }
