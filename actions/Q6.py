import tkinter as tk
from utils import display
from utils import db
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# def read_csv_file_temp_by_month(csvFile, separator, filter_year, filter_department):
#     df = pd.read_csv(csvFile, sep=separator)
#     df = df.where(pd.notnull(df), 'null')
#
#     #Changement de format
#     df['date_obs'] = pd.to_datetime(df['date_obs'])
#
#     #Filtre l'annee et département
#     df_filtered = df[
#         (df['date_obs'].dt.year == int(filter_year)) &
#         (df['departement'] == filter_department)
#         ]
#
#     #On prend que les mois
#     df_filtered['month'] = df_filtered['date_obs'].dt.month
#
#     #Regroupe par mois et calcule la moyenne temperature de chaque mois
#     df_grouped = df_filtered.groupby('month').agg({'tmin': 'mean'}).reset_index()
#
#     #Plot
#     fig = px.line(df_grouped, x='month', y='tmin', title=f'Temperature for {filter_department} in {filter_year}', labels={'tmin': 'Average Temperature'})
#     fig.show()
#     return df_filtered
# read_csv_file_temp_by_month('data/csv/Mesures.csv', ';', '2022', 'Isère')

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(1000, 600, self)
        self.title('F4 : températures en isère en 2022')
        display.defineGridDisplay(self, 1, 1)

        query = """
            SELECT strftime('%Y-%m-%d', date_mesure) as month_year, AVG(temperature_min_mesure) as avg_temp_min
            FROM Mesures
            WHERE code_departement = 'Isère' AND strftime('%Y', date_mesure) = '2022'
            GROUP BY month_year
            ORDER BY month_year
        """

        # Extraction des données et affichage dans le tableau
        result = []
        try:
            cursor = db.data.cursor()
            result = cursor.execute(query)
        except Exception as e:
            print("Erreur : " + repr(e))

        # Extraction et préparation des valeurs à mettre sur le graphique

        tabmin = []

        tabx = []
        for row in result:

            tabx.append(row[0])
            tabmin.append(row[2])


        # Formatage des dates pour l'affichage sur l'axe x
        datetime_dates = [datetime.strptime(date, '%Y-%m-%d') for date in tabx]

        # Ajout de la figure et du subplot qui contiendront le graphique
        fig = Figure(figsize=(10, 6), dpi=100)
        plot1 = fig.add_subplot(111)

        # Affichage des courbes

        plot1.plot(range(len(datetime_dates)), tabmin, color='b', label='temp. min')

        # Configuration de l'axe x pour n'afficher que le premier jour de chaque mois
        xticks = [i for i, date in enumerate(datetime_dates) if date.day == 1]
        xticklabels = [date.strftime('%m-%d') for date in datetime_dates if date.day == 1]
        plot1.set_xticks(xticks)
        plot1.set_xticklabels(xticklabels, rotation=45)
        plot1.legend()

        # Affichage du graphique
        canvas = FigureCanvasTkAgg(fig,  master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()
