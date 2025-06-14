from views.menu import Menu
from controllers.playercontroller import JoueurController
from controllers.tournamentcontroller import TournamentController
from views.rapport import Rapport


def main():
    """Exécute le programme principal de gestion des tournois."""
    joueur_controller = JoueurController()
    tournoi_controller = TournamentController()

    while True:
        choix = Menu.afficher_menu_principal()
        if choix is None or choix.lower() == "q":
            print("Au revoir !")
            break

        if choix == "1":
            while True:
                sous_choix = Menu.afficher_menu_joueur()
                if sous_choix is None or sous_choix.lower() == "q":
                    break

                if sous_choix == "1":
                    if joueur_controller.creer_joueur() is None:
                        break
                elif sous_choix == "2":
                    joueur_controller.lister_joueurs()
                elif sous_choix == "3":
                    break
                else:
                    print("Choix invalide")

        elif choix == "2":
            while True:
                sous_choix1 = Menu.afficher_menu_tournois()
                if sous_choix1 is None or sous_choix1.lower() == "q":
                    break
                if sous_choix1 == "1":
                    tournoi = tournoi_controller.creer_nouveau_tournoi()
                    if tournoi is None:
                        break
                    if not tournoi_controller.jouer_tournoi(tournoi):
                        break
                elif sous_choix1 == "2":
                    if tournoi_controller.continuer_tournoi() is None:
                        break
                elif sous_choix1 == "3":
                    break
                else:
                    print("Choix invalide")
        elif choix == "3":
            termines = Rapport.afficher_tournois_termines()
            if termines:
                selection = input("\nNuméro du tournoi pour voir le "
                                  "rapport (ou 'q' pour quitter) : ").strip()
                if selection.lower() == "q":
                    continue
                if selection.isdigit():
                    numero = int(selection)
                    if numero > 0 and numero <= len(termines):
                        tournoi_selectionne = termines[numero - 1]
                        Rapport.afficher_classement_et_resultats(
                            tournoi_selectionne)
                    else:
                        print("Numéro invalide.")
                else:
                    print("Entrée invalide.")

        elif choix == "4":
            print("Au revoir !")
            break

        else:
            print("Choix invalide")


if __name__ == "__main__":
    main()
