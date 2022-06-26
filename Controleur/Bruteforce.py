# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
from rich.table import Table
PRIX = 2
RENDEMENT = 4

# Définition de la classe


class Bruteforce:
    """
    Permet la recherche des actions les plus pertinentes dans un fichier .csv en bruteforce
    """
    def __init__(self, modele):
        self.modele = modele

    def chercher_rentabilite(self) -> [list]:
        """
        Recherche la meilleure action en fonction du rendement
        :return: [list]
        """
        self.modele.max_rentabilite = 0
        for index, action in enumerate(self.modele.actions):
            if action[RENDEMENT] > self.modele.max_rentabilite:
                self.modele.max_rentabilite = action[RENDEMENT]
                self.modele.meilleur_action = action
                self.modele.index_action = index
        return self.modele.meilleur_action

    def calculer_budget(self) -> [list]:
        """
        Achète l'action si le budget est supérieur ou egal au prix de l'action
        :return: [list]
        """
        if self.modele.budget >= self.modele.meilleur_action[PRIX]:
            self.modele.budget = self.modele.budget - self.modele.meilleur_action[PRIX]
            self.modele.gain = self.modele.gain + self.modele.meilleur_action[RENDEMENT]
            self.modele.resultat.append([self.modele.meilleur_action,
                                         round(self.modele.budget, 2),
                                         round(self.modele.gain, 2)])
            self.modele.actions.pop(self.modele.index_action)
        else:
            self.modele.actions.pop(self.modele.index_action)
        return self.modele.resultat

    def executer(self):
        """
        Execute la recherche en force brute
        :return: [list]
        """
        self.modele.supprimer_action_nul()
        while True:
            if self.modele.actions:
                Bruteforce.chercher_rentabilite(self)
                Bruteforce.calculer_budget(self)
            else:
                return False

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
