# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
from operator import itemgetter
#############################################
# Définition des constantes
PRIX = 2
PROFIT = 3
PROFIT_REEL = 4
# Définition de la classe


class Optimized:
    """
      Permet la recherche des actions les plus pertinentes dans un fichier en version optimisé .csv
    """
    def __init__(self, modele):
        self.modele = modele

    def trier_liste(self) -> [list]:
        """
        Trie la liste par profit du plus élevé au plus faible
        :return: [list]
        """
        self.modele.actions.sort(key=itemgetter(PROFIT), reverse=True)
        return self.modele.actions

    def executer(self) -> [list]:
        """
        Executer la recherche en optimisé
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
