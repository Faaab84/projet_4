from models.tournament import Tournois


class Rapport:
    """Affiche les informations sur les tournois terminés et leurs résultats."""

    @staticmethod
    def afficher_tournois_termines():
        """Affiche la liste des tournois terminés."""
        tournois = Tournois.from_fichier()
        termines = []
        for t in tournois:
            if t.etat == "Terminé":
                termines.append(t)
        if not termines:
            print("\nAucun tournoi terminé.")
            return None
        print("\n=== Tournois terminés ===")
        for idx, tournoi in enumerate(termines, 1):
            print(f"{idx}. {tournoi.nom} ({tournoi.lieu}, {tournoi.date})")
        return termines

    @staticmethod
    def afficher_classement_et_resultats(tournoi):
        """Affiche le classement des joueurs et les résultats des matchs."""
        joueurs_scores = []
        for joueur in tournoi.joueurs:
            score = joueur.score or 0
            joueurs_scores.append([joueur, score])

        for i in range(len(joueurs_scores)):
            for j in range(i + 1, len(joueurs_scores)):
                if joueurs_scores[i][1] < joueurs_scores[j][1]:
                    joueurs_scores[i], joueurs_scores[j] = joueurs_scores[j], joueurs_scores[i]

        print(f"\n=== Classement du tournoi '{tournoi.nom}' ===")
        for idx, (joueur, score) in enumerate(joueurs_scores, 1):
            print(f"{idx}. {joueur.prenom} {joueur.nom} - {score} points")

        print(f"\n=== Résultats des matchs du tournoi '{tournoi.nom}' ===")
        for tour in tournoi.tours:
            print(f"\n--- {tour.nom} ---")
            for match in tour.matchs:
                score1 = match.scorej1 or "-"
                score2 = match.scorej2 or "-"
                print(f"{match.joueur1.prenom} {match.joueur1.nom} ({score1}) "
                      f"vs {match.joueur2.prenom} {match.joueur2.nom} "
                      f"({score2})")
