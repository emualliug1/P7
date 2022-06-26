# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
from operator import itemgetter
from rich.table import Table
#############################################
# Définition des constantes
PRIX = 2
RENDEMENT = 4
PROFIT = 3
# Définition de la classe


class Optimized:
    """
      Permet la recherche des actions les plus pertinentes dans un fichier .csv
    """
    def __init__(self, modele):
        self.modele = modele

    def trier_liste(self) -> [list]:
        """
        Trie la liste par rendement du plus élevé au plus faible
        :return: [list]
        """
        self.modele.actions.sort(key=itemgetter(RENDEMENT), reverse=True)
        return self.modele.actions

    def executer(self) -> [list]:
        """
        Executer la recherche en optimized
        :return: [list]
        """
        self.modele.supprimer_action_nul()
        self.modele.resultat = []
        self.modele.gain = 0
        Optimized.trier_liste(self)
        for action in self.modele.actions:
            if action[PRIX] <= self.modele.budget:
                self.modele.budget = self.modele.budget - action[PRIX]
                self.modele.gain = self.modele.gain + action[4]
                self.modele.resultat.append([action,
                                             round(self.modele.budget, 2),
                                             round(self.modele.gain, 2)])
        return self.modele.resultat

    def remplir_tableau(self) -> [Table]:
        """
        Creer un tableau pour le resultat de la recherche
        :return: [Table]
        """
        self.modele.creer_tableau()
        for action in self.modele.resultat:
            self.modele.tableau.add_row(
                str(action[0][0]),
                str(action[0][1]),
                str(action[0][2]),
                str(action[0][3]),
                str(action[0][4]),
                str(action[1]),
                str(action[2]))
        return self.modele.tableau


