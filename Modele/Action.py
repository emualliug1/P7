# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
import pandas as pd
from rich.table import Table
from rich import box
#############################################
# Définition des constantes
RENDEMENT = 4
# Définition de la classe


class Action:
    """
    Récupération des actions dans le fichier csv
    """
    def __init__(self, fichier):
        self.fichier: None = fichier
        self.liste_actions: list = []
        self.budget: float = 500
        self.actions: list = []
        self.meilleur_action: list = []
        self.max_rentabilite: float = 0
        self.index_action: int = 0
        self.resultat: list = []
        self.gain: float = 0
        self.tableau = Table

    def transformer_liste(self) -> [list]:
        """
        Transformation d'un fichier .csv en une liste avec pandas
        :return:[list]
        """
        data = pd.read_csv(self.fichier)
        data['rendement'] = round(data['price'] * (data['profit'] / 100), 2)
        row_index = data.index.tolist()
        row_name = data["name"].tolist()
        row_price = data["price"].tolist()
        row_profit = data["profit"].tolist()
        row_rendement = data["rendement"].tolist()
        for i, j, k, l, m in zip(row_index, row_name, row_price, row_profit, row_rendement):
            self.liste_actions.append([i, j, k, l, m])
        return self.liste_actions

    def supprimer_action_nul(self) -> [list]:
        """
        Supprime toutes les actions qui ont un rendement inférieur ou egal à 0
        :return:[list]
        """
        Action.transformer_liste(self)
        for action in self.liste_actions:
            if action[RENDEMENT] > 0:
                self.actions.append(action)
        return self.actions

    def creer_tableau(self) -> [Table]:
        """
        Cree un tableau avec l'affichage des différents critères d'une action
        :return:[Table]
        """
        self.tableau = Table(box=box.HORIZONTALS, show_header=True, header_style='bold')
        self.tableau.add_column('Id')
        self.tableau.add_column('Nom')
        self.tableau.add_column('Prix(€)')
        self.tableau.add_column('Profit(%)')
        self.tableau.add_column('Rendement(€)')
        self.tableau.add_column('Budget(€)')
        self.tableau.add_column('Gain(€)')
        return self.tableau
