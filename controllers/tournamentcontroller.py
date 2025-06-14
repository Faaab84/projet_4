from models.player import Joueur
from models.tournament import Tournois
from models.match import Match
from models.round import Round
from views.tournament import TournamentCreation
from views.rapport import Rapport
from datetime import datetime
import random


class TournamentController:
    """Gère les tournois d'échecs en coordonnant modèle et vue."""

    def creer_nouveau_tournoi(self):
        """Crée un nouveau tournoi avec les informations utilisateur."""
        while True:
            TournamentCreation.display_prompt_tournament_name()
            nom = input().strip()
            if nom.lower() == "q":
                return None
            if nom == "":
                TournamentCreation.display_error_empty_name()
                continue
            break

        while True:
            TournamentCreation.display_prompt_location()
            lieu = input().strip()
            if lieu.lower() == "q":
                return None
            if lieu == "":
                TournamentCreation.display_error_empty_location()
                continue
            break

        infos = TournamentCreation.demander_infos_tournoi()
        if infos is None:
            return None
        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        joueurs_disponibles = Joueur.read_json()
        if len(joueurs_disponibles) < 2:
            TournamentCreation.display_error_insufficient_players()
            return None

        TournamentCreation.display_available_players()
        for idx, joueur in enumerate(joueurs_disponibles, 1):
            TournamentCreation.display_player(idx, joueur)

        while True:
            TournamentCreation.display_prompt_player_selection()
            selection = input().strip()
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
                TournamentCreation.display_error_invalid_selection()
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

        self.creer_tour(tournoi, round_number=0)
        tournoi.save()

        TournamentCreation.display_tournament_created(tournoi, len(joueurs_selectionnes))
        TournamentCreation.display_round_title(tournoi.tours[0].nom)
        tournoi.tours[0].afficher_matchs()
        return tournoi

    def creer_tour(self, tournoi, round_number):
        """Génère un nouveau tour avec des appariements uniques."""
        joueurs_pairs = self.creer_paires_joueurs(tournoi, round_number)
        if not joueurs_pairs:
            TournamentCreation.display_no_valid_pairs()
            tournoi.etat = "Terminé"
            tournoi.save()
            return

        nom_tour = f"Tour {round_number + 1}"
        date_debut = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        nouveau_tour = Round(nom_tour, tournoi.joueurs, date_debut, "")
        nouveau_tour.matchs = [Match(j1, j2) for j1, j2 in joueurs_pairs]
        tournoi.tours.append(nouveau_tour)
        for j1, j2 in joueurs_pairs:
            paire = [j1.identifiant_national, j2.identifiant_national]
            tournoi.paires_jouees.append(paire)

    def creer_paires_joueurs(self, tournoi, round_number):
        """Génère des paires de joueurs uniques pour un tour."""
        nombre_joueurs = len(tournoi.joueurs)
        max_paires = (nombre_joueurs * (nombre_joueurs - 1)) // 2
        if len(tournoi.paires_jouees) >= max_paires:
            return []
        if round_number == 0:
            sorted_players = tournoi.joueurs.copy()
            random.shuffle(sorted_players)
        else:
            sorted_players = sorted(
                tournoi.joueurs,
                key=lambda x: self.get_score_total(tournoi, x),
                reverse=True
            )

        joueurs_pairs = []
        used_players = set()
        for i, player1 in enumerate(sorted_players):
            if player1 in used_players:
                continue
            for j in range(i + 1, len(sorted_players)):
                player2 = sorted_players[j]
                if player2 in used_players:
                    continue
                paire = [player1.identifiant_national, player2.identifiant_national]
                paire_inversee = [player2.identifiant_national, player1.identifiant_national]
                if paire not in tournoi.paires_jouees and paire_inversee not in tournoi.paires_jouees:
                    joueurs_pairs.append((player1, player2))
                    used_players.add(player1)
                    used_players.add(player2)
                    break
            else:
                continue

        if not joueurs_pairs:
            return []

        return joueurs_pairs

    def get_score_total(self, tournoi, joueur):
        """Calcule le score total d'un joueur dans le tournoi."""
        score = 0.0
        for tour in tournoi.tours:
            for match in tour.matchs:
                if match.joueur1.identifiant_national == joueur.identifiant_national:
                    score += match.scorej1 or 0
                elif match.joueur2.identifiant_national == joueur.identifiant_national:
                    score += match.scorej2 or 0
        return score

    def continuer_tournoi(self):
        """Reprend un tournoi en cours parmi ceux disponibles."""
        tournois = Tournois.from_fichier()
        en_cours = []
        for t in tournois:
            if t.etat == "En cours":
                en_cours.append(t)

        if not en_cours:
            TournamentCreation.display_no_ongoing_tournaments()
            return None

        TournamentCreation.display_ongoing_tournaments()
        for idx, tournoi in enumerate(en_cours, 1):
            TournamentCreation.display_tournament(idx, tournoi)

        while True:
            TournamentCreation.display_prompt_tournament_selection()
            choix = input().strip()
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
                    TournamentCreation.display_error_invalid_tournament_number()
            except ValueError:
                TournamentCreation.display_error_invalid_input()

    def jouer_tournoi(self, tournoi):
        """Gère la progression d'un tournoi avec saisie des résultats."""
        if tournoi.tours and tournoi.tours[-1].etat != "Terminé":
            if not self.saisir_resultats_tournoi(tournoi):
                return False

        while len(tournoi.tours) < tournoi.nombre_tours and tournoi.etat == "En cours":
            self.creer_tour(tournoi, round_number=len(tournoi.tours))
            if tournoi.etat == "Terminé":
                break
            TournamentCreation.display_round_title(tournoi.tours[-1].nom)
            tournoi.tours[-1].afficher_matchs()
            if not self.saisir_resultats_tournoi(tournoi):
                return False
            tournoi.save()

        tournoi.etat = "Terminé"
        tournoi.save()
        Rapport.afficher_classement_et_resultats(tournoi)
        return True

    def saisir_resultats_tournoi(self, tournoi):
        """Enregistre les résultats des matchs pour le tour actuel."""
        for tour in tournoi.tours:
            if tour.etat == "Terminé":
                continue
            TournamentCreation.display_round_title(tour.nom)
            tour.demarrer()
            for match in tour.matchs:
                if match.scorej1 is not None and match.scorej2 is not None:
                    continue
                resultat = TournamentCreation.demander_resultat_match(match)
                if resultat is None:
                    tournoi.save()
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
            tournoi.save()
        return True
