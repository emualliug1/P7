# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
from Controleur import Bruteforce
from Controleur import Optimized
from Modele import Action
from Vue import Affichage
from rich.live import Live
from rich.panel import Panel
import cProfile
import io
import pstats
#############################################


def main():
    modele_bruteforce = Action('Data/dataset0.csv')
    modele_optimized = Action('Data/dataset2.csv')

    vue = Affichage()

    bruteforce = Bruteforce(modele_bruteforce)
    optimized = Optimized(modele_optimized)

    bf_profile = cProfile.Profile()
    bf_io = io.StringIO()
    bf_profile.enable()
    bruteforce.executer()
    bf_profile.disable()
    brute_force_stats = pstats.Stats(bf_profile, stream=bf_io).sort_stats('ncalls')
    brute_force_stats.print_stats()
    bf_stats = str((bf_io.getvalue()))

    opti_profile = cProfile.Profile()
    opti_io = io.StringIO()
    opti_profile.enable()
    optimized.executer()
    opti_profile.disable()
    optimized_stats = pstats.Stats(opti_profile, stream=opti_io).sort_stats('ncalls')
    optimized_stats.print_stats()
    opti_stats = str((opti_io.getvalue()))

    with Live(vue.creer_ecran(), refresh_per_second=0.5, screen=True):
        vue.ecran_bruteforce_resultat.update(Panel(bruteforce.modele.creer_tableau(),
                                                   title='Brute Force', border_style='red'))
        vue.ecran_bruteforce_profiler.update(Panel(bf_stats,
                                                   title='Profiler', border_style='red'))

        vue.ecran_optimized_resultat.update(Panel(optimized.modele.creer_tableau(),
                                                  title='Optimized', border_style='blue'))
        vue.ecran_optimized_profiler.update(Panel(opti_stats,
                                                  title='Profiler', border_style='blue'))
        vue.pause_ecran()

if __name__ == "__main__":

    main()
