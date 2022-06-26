from rich.layout import Layout
from rich.console import Console


class Affichage(Console):
    def __init__(self):
        Console.__init__(self)
        self.ecran = Layout(name='root')
        self.ecran_bruteforce = Layout(name='brute force')
        self.ecran_bruteforce_resultat = Layout(name='bruteforce_resultat', ratio=5)
        self.ecran_bruteforce_profiler = Layout(name='bruteforce_profiler', ratio=4)
        self.ecran_optimized = Layout(name='optimized')
        self.ecran_optimized_resultat = Layout(name='optimized_resultat', ratio=5)
        self.ecran_optimized_profiler = Layout(name='optimized_profiler', ratio=4)

    @staticmethod
    def pause_ecran():
        """Met l'écran en pause dans la console"""
        input()

    def creer_ecran(self):
        """Créer l'écran de la console en la divisant en case"""
        self.ecran.split_row(
            self.ecran_bruteforce,
            self.ecran_optimized
        )
        self.ecran_bruteforce.split_column(
            self.ecran_bruteforce_resultat,
            self.ecran_bruteforce_profiler
        )
        self.ecran_optimized.split_column(
            self.ecran_optimized_resultat,
            self.ecran_optimized_profiler
        )
        return self.ecran
