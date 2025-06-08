from models.player import Joueur
from models.tournament import Tournois
from models.match import Match
from models.round import Round
from views.tournament import TournamentCreation
from views.rapport import Rapport
from datetime import datetime
import random
import json
import os


class TournamentController:
    """Crée un nouveau tournoi en demandant les informations
       nécessaires et en sélectionnant les joueurs"""
    def creer_nouveau_tournoi(self):
        while True:
            nom = input("Nom du tournoi (ou 'q' pour quitter) : ").strip()
            if nom.lower() == "q":
                return None
            if nom == "":
                print("Le nom du tournoi ne peut pas être vide.")
                continue
            break

        while True:
            lieu = input("Lieu du tournoi (ou 'q' pour quitter) : ").strip()
            if lieu.lower() == "q":
                return None
            if lieu == "":
                print("Le lieu ne peut pas être vide.")
                continue
            break

        infos = TournamentCreation.demander_infos_tournoi()
        if infos is None:
            return None
        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        joueurs_disponibles = Joueur.read_json()
        if len(joueurs_disponibles) < 2:
            print("Erreur : il faut au moins 2 joueurs pour créer un tournoi.")
            return None

        print("\nListe des joueurs disponibles :")
        for idx, joueur in enumerate(joueurs_disponibles, 1):
            print(f"{idx}. {joueur.prenom} {joueur.nom}")

        while True:
            selection = input(
                "Numéros des joueurs à inscrire (séparés par des virgules, "
                "ou 'q' pour quitter) : ").strip()
            if selection.lower() == "q":
                return None
            indices = []
            for i in selection.split(","):
                if i.strip().isdigit():
                    indices.append(int(i.strip()) - 1)
            joueurs_selectionnes = []
            for i in indices:
                if 0 <= i < len(joueurs_disponibles):
                    joueurs_selectionnes.append(joueurs_disponibles[i])
            if len(joueurs_selectionnes) < 2:
                print("Erreur : il faut sélectionner au moins 2 joueurs.")
            else:
                break

        tournoi = Tournois(
            nom=nom,
            lieu=lieu,
            date=date,
            nombre_tours=infos['nombre_tours'],
            description=infos['description']
        )
        tournoi.joueurs = joueurs_selectionnes
        tournoi.paires_jouees = []

        self.generer_premier_tour(tournoi)
        self.sauvegarder_tournoi(tournoi)

        print(
            f"\nTournoi '{tournoi.nom}' créé avec {len(joueurs_selectionnes)} "
            f"joueurs et {tournoi.nombre_tours} tours !")
        print(f"\n--- {tournoi.tours[0].nom} ---")
        tournoi.tours[0].afficher_matchs()
        return tournoi

    """ Génère le premier tour d'un tournoi en mélangeant
    les joueurs et en créant les paires"""
    def generer_premier_tour(self, tournoi):
        random.shuffle(tournoi.joueurs)
        nom_tour = "Tour 1"
        date_debut = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        round1 = Round(nom_tour, tournoi.joueurs, date_debut, "")
        round1.generer_paire()
        for match in round1.matchs:
            paire = [match.joueur1.identifiant_national,
                     match.joueur2.identifiant_national]
            tournoi.paires_jouees.append(paire)
        tournoi.tours = [round1]

    # Calcule le score total d'un joueur dans un tournoi donné
    def get_score_total(self, tournoi, joueur):
        score = 0.0
        for tour in tournoi.tours:
            for match in tour.matchs:
                if match.joueur1.identifiant_national ==\
                        joueur.identifiant_national:
                    score += match.scorej1 or 0
                elif match.joueur2.identifiant_national ==\
                        joueur.identifiant_national:
                    score += match.scorej2 or 0
        return score

    """ Génère le tour suivant en triant les joueurs
     par score et en créant de nouvelles paires"""
    def generer_tour_suivant(self, tournoi):
        nombre_joueurs = len(tournoi.joueurs)
        max_paires = (nombre_joueurs * (nombre_joueurs - 1)) // 2
        if len(tournoi.paires_jouees) >= max_paires:
            print("Tous les joueurs ont joué contre tous les autres"
                  ", le tournoi est terminé !")
            tournoi.etat = "Terminé"
            self.sauvegarder_tournoi(tournoi)
            return

        joueurs_scores = []
        for joueur in tournoi.joueurs:
            score = self.get_score_total(tournoi, joueur)
            joueurs_scores.append([joueur, score])

        for i in range(len(joueurs_scores)):
            for j in range(i + 1, len(joueurs_scores)):
                if joueurs_scores[i][1] < joueurs_scores[j][1]:
                    joueurs_scores[i], joueurs_scores[j] = \
                        joueurs_scores[j], joueurs_scores[i]

        joueurs_tries = []
        for joueur, score in joueurs_scores:
            joueurs_tries.append(joueur)

        paires = []
        utilises = []
        for i in range(len(joueurs_tries)):
            joueur1 = joueurs_tries[i]
            if joueur1 in utilises:
                continue
            for j in range(i + 1, len(joueurs_tries)):
                joueur2 = joueurs_tries[j]
                if joueur2 in utilises:
                    continue
                paire = [joueur1.identifiant_national,
                         joueur2.identifiant_national]
                paire_inversee = [joueur2.identifiant_national,
                                  joueur1.identifiant_national]
                if paire not in tournoi.paires_jouees and paire_inversee \
                        not in tournoi.paires_jouees:
                    paires.append([joueur1, joueur2])
                    tournoi.paires_jouees.append(paire)
                    utilises.append(joueur1)
                    utilises.append(joueur2)
                    break

        if not paires:
            print("Plus de matchs possibles, le tournoi est terminé !")
            tournoi.etat = "Terminé"
            self.sauvegarder_tournoi(tournoi)
            return

        nom_tour = f"Tour {len(tournoi.tours) + 1}"
        date_debut = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        nouveau_tour = Round(nom_tour, tournoi.joueurs, date_debut, "")
        nouveau_tour.matchs = []
        for joueur1, joueur2 in paires:
            match = Match(joueur1, joueur2)
            nouveau_tour.matchs.append(match)
        tournoi.tours.append(nouveau_tour)

    # Sauvegarde le tournoi dans un fichier JSON
    def sauvegarder_tournoi(self, tournoi, fichier="tournois.json"):
        data = []
        if os.path.exists(fichier):
            with open(fichier, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

        new_data = []
        for t in data:
            if t.get("nom") != tournoi.nom or t.get("date") != tournoi.date:
                new_data.append(t)
        data = new_data

        data.append(tournoi.to_save())
        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    """ Permet de continuer un tournoi en cours en
    sélectionnant parmi les tournois disponibles"""
    def continuer_tournoi(self):
        tournois = Tournois.from_fichier()
        en_cours = []
        for t in tournois:
            if t.etat == "En cours":
                en_cours.append(t)

        if not en_cours:
            print("Aucun tournoi en cours à continuer.")
            return None

        print("\nTournois en cours :")
        for idx, tournoi in enumerate(en_cours, 1):
            print(f"{idx}. {tournoi.nom} ({tournoi.lieu}, {tournoi.date})")

        while True:
            choix = input("Numéro du tournoi à continuer "
                          "(ou 'q' pour quitter) : ").strip()
            if choix.lower() == "q":
                return None
            try:
                idx = int(choix) - 1
                if 0 <= idx < len(en_cours):
                    tournoi = en_cours[idx]
                    if not self.jouer_tournoi(tournoi):
                        return None
                    return tournoi
                else:
                    print("Numéro invalide.")
            except ValueError:
                print("Entrée invalide.")

    """Gère le déroulement d'un tournoi, y compris la saisie
    des résultats et la génération des tours"""
    def jouer_tournoi(self, tournoi):
        if tournoi.tours and tournoi.tours[-1].etat != "Terminé":
            if not self.saisir_resultats_tournoi(tournoi):
                return False

        while len(tournoi.tours) < tournoi.nombre_tours and\
                tournoi.etat == "En cours":
            self.generer_tour_suivant(tournoi)
            if tournoi.etat == "Terminé":
                break
            print(f"\n--- {tournoi.tours[-1].nom} ---")
            tournoi.tours[-1].afficher_matchs()
            if not self.saisir_resultats_tournoi(tournoi):
                return False
            self.sauvegarder_tournoi(tournoi)

        tournoi.etat = "Terminé"
        self.sauvegarder_tournoi(tournoi)
        Rapport.afficher_classement_et_resultats(tournoi)
        return True

    # Saisit les résultats des matchs pour le tour actuel d'un tournoi
    def saisir_resultats_tournoi(self, tournoi):
        for tour in tournoi.tours:
            if tour.etat == "Terminé":
                continue
            print(f"\n--- {tour.nom} ---")
            tour.demarrer()
            for match in tour.matchs:
                if match.scorej1 is not None and match.scorej2 is not None:
                    continue
                resultat = TournamentCreation.demander_resultat_match(match)
                if resultat is None:
                    self.sauvegarder_tournoi(tournoi)
                    return False
                if resultat == "1":
                    match.resultat(1, 0)
                    match.joueur1.score += 1
                    match.joueur2.score += 0
                elif resultat == "2":
                    match.resultat(0, 1)
                    match.joueur1.score += 0
                    match.joueur2.score += 1
                elif resultat == "3":
                    match.resultat(0.5, 0.5)
                    match.joueur1.score += 0.5
                    match.joueur2.score += 0.5
            tour.terminer()
            self.sauvegarder_tournoi(tournoi)
        return True
