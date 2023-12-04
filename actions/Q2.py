import tkinter as tk
from utils import display
from tkinter import ttk

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(600, 400, self)
        self.title('Q2 : département le plus froid par région')
        display.defineGridDisplay(self, 2, 1)
        ttk.Label(self, text="Modifier cette fonction en s'inspirant du code de F1, pour qu'elle affiche le(s) département(s) avec la température moyenne (c.a.d. moyenne des moyennes de toutes les mesures) la plus basse. \nSchéma attendu : (nom_region, nom_departement, temperature_moy_min)",
                  wraplength=500, anchor="center", font=('Helvetica', '10', 'bold')).grid(sticky="we", row=0)

        #TODO Q2 Modifier la suite du code (en se basant sur le code de F1) pour répondre à Q2

        # On définit les colonnes que l'on souhaite afficher dans la fenêtre et la requête
        columns = ('nom_region', 'nom_departement', 'temperature_moy_min')
        query = """
                  WITH avg_temperature_departement AS (
                  SELECT code_departement, AVG(temperature_moy_mesure) AS avg_temp_dpt FROM Mesures
                  GROUP BY code_departement),
                  min_avg_temp_par_region AS (
                  SELECT D.code_region, MIN(A.avg_temp_dpt) AS min_avg_temp_region 
                  FROM Departements D JOIN avg_temperature_departement A ON D.code_departement = A.code_departement
                  GROUP BY D.code_region)
                  SELECT R.nom_region, D.nom_departement, A.avg_temp_dpt AS temperature_moy_min
                  FROM Regions R JOIN Departements D USING (code_region) JOIN avg_temperature_departement A USING (code_departement) JOIN min_avg_temp_par_region M ON D.code_region = M.code_region AND A.avg_temp_dpt = M.min_avg_temp_region;"""

        # On utilise la fonction createTreeViewDisplayQuery pour afficher les résultats de la requête
        tree = display.createTreeViewDisplayQuery(self, columns, query,200)
        tree.grid(row=0, sticky="nswe")
     
