from flask import Flask, render_template, jsonify
import pandas as pd
import folium
import plotly.express as px
import plotly.io as pio

# Initialiser Flask
app = Flask(__name__)

# Charger les fichiers CSV
def load_patients_data():
    file_path = '../patients_by_region.csv'  # Remplacer par le chemin correct
    df = pd.read_csv(file_path)
    if not {'Region Name', 'Latitude', 'Longitude', 'Patient Count'}.issubset(df.columns):
        raise KeyError("Les colonnes 'Region Name', 'Latitude', 'Longitude', ou 'Patient Count' manquent dans le fichier.")
    return df

def load_prevalence_data():
    file_path = '../prevalence_by_year.csv'  # Remplacer par le chemin correct
    df = pd.read_csv(file_path)
    if not {'Year', 'Average Prevalence'}.issubset(df.columns):
        raise KeyError("Les colonnes 'Year' ou 'Average Prevalence' manquent dans le fichier.")
    return df

def load_prevalence_by_gender_year():
    file_path = '../prevalence_by_gender_year.csv'  # Remplacer par le chemin correct
    df = pd.read_csv(file_path)
    if not {'Year', 'Gender Label', 'Average Prevalence'}.issubset(df.columns):
        raise KeyError("Les colonnes 'Year', 'Gender Label' ou 'Average Prevalence' manquent dans le fichier.")
    return df


def load_prevalence_by_pathology_level1():
    # Charger les données de prévalence par pathologie de niveau 1
    file_path = '../prevalence_by_pathology_level1.csv'  # Remplacer par le chemin correct
    df = pd.read_csv(file_path)
    if not {'Pathology Name', 'Average Prevalence'}.issubset(df.columns):
        raise KeyError("Les colonnes 'Pathology' ou 'Average Prevalence' manquent dans le fichier.")
    return df

def load_prevalence_by_pathology_level2():
    # Charger les données de prévalence par pathologie de niveau 1
    file_path = '../prevalence_by_pathology_level2.csv'  # Remplacer par le chemin correct
    df = pd.read_csv(file_path)
    if not {'Pathology Name', 'Average Prevalence'}.issubset(df.columns):
        raise KeyError("Les colonnes 'Pathology' ou 'Average Prevalence' manquent dans le fichier.")
    return df

def load_prevalence_by_pathology_level3():
    # Charger les données de prévalence par pathologie de niveau 1
    file_path = '../prevalence_by_pathology_level3.csv'  # Remplacer par le chemin correct
    df = pd.read_csv(file_path)
    if not {'Pathology Name', 'Average Prevalence'}.issubset(df.columns):
        raise KeyError("Les colonnes 'Pathology' ou 'Average Prevalence' manquent dans le fichier.")
    return df


# Route pour afficher la carte
@app.route('/map')
def map_view():
    try:
        df = load_patients_data()
        map_center = [46.603354, 1.888334]
        m = folium.Map(location=map_center, zoom_start=6)

        for _, row in df.iterrows():
            if not pd.isna(row['Latitude']) and not pd.isna(row['Longitude']):
                folium.Marker(
                    location=[row['Latitude'], row['Longitude']],
                    popup=f"{row['Region Name']}<br>Patients: {row['Patient Count']}",
                    tooltip=row['Region Name']
                ).add_to(m)

        map_file = 'templates/map.html'
        m.save(map_file)
        return render_template('map.html')
    except Exception as e:
        return f"Erreur : {str(e)}", 500

# Route pour afficher le scatter plot
@app.route('/scatter')
def scatter_plot():
    try:
        prevalence_df = load_prevalence_data()
        fig = px.scatter(
            prevalence_df,
            x='Year',
            y='Average Prevalence',
            title='Évolution de la Prévalence par Année',
            labels={'Year': 'Année', 'Average Prevalence': 'Prévalence moyenne'},
            template='plotly_dark'
        )
        fig.update_traces(mode='lines+markers', marker=dict(size=8))
        scatter_html = pio.to_html(fig, full_html=False)
        return render_template('scatter.html', scatter_html=scatter_html)
    except Exception as e:
        return f"Erreur : {str(e)}", 500

@app.route('/pie/<int:year>')
def pie_chart(year):
    try:
        prevalence_df = load_prevalence_by_gender_year()
        filtered_data = prevalence_df[prevalence_df['Year'] == year]

        if filtered_data.empty:
            return f"Aucune donnée trouvée pour l'année {year}.", 404

        fig = px.pie(
            filtered_data,
            values='Average Prevalence',
            names='Gender Label',
            title=f'Prévalence par Sexe pour l\'année {year}',
            template='plotly_dark'
        )
        pie_html = pio.to_html(fig, full_html=False)
        return render_template('pie.html', pie_html=pie_html)
    except Exception as e:
        return f"Erreur : {str(e)}", 500

@app.route('/histogram/level1')
def histogram_level1():
    try:
        # Charger les données de prévalence par pathologie de niveau 1
        prevalence_by_pathology_level1_df = load_prevalence_by_pathology_level1()

        # Créer l'histogramme de niveau 1 avec des barres horizontales
        fig1 = px.histogram(
            prevalence_by_pathology_level1_df,
            x='Average Prevalence',  # On utilise x pour la prévalence
            y='Pathology Level 1',   # Et y pour la pathologie
            title='Histogramme de la Prévalence par Pathologie de Niveau 1',
            labels={'Average Prevalence': 'Prévalence Moyenne', 'Pathology Level 1': 'Pathologie'},
            template='plotly_dark',
            orientation='h'  # L'option 'h' pour des barres horizontales
        )
        histogram1_html = pio.to_html(fig1, full_html=False)

        return render_template('histogram_level1.html', histogram_html=histogram1_html)

    except Exception as e:
        return f"Erreur : {str(e)}", 500

@app.route('/histogram/level2')
def histogram_level2():
    try:
        # Charger les données de prévalence par pathologie de niveau 2
        prevalence_by_pathology_level2_df = load_prevalence_by_pathology_level2()

        # Créer l'histogramme de niveau 2 avec des barres horizontales
        fig2 = px.histogram(
            prevalence_by_pathology_level2_df,
            x='Average Prevalence',
            y='Pathology Level 2',
            title='Histogramme de la Prévalence par Pathologie de Niveau 2',
            labels={'Average Prevalence': 'Prévalence Moyenne', 'Pathology Level 2': 'Pathologie'},
            template='plotly_dark',
            orientation='h'  # Utilisation de 'h' pour des barres horizontales
        )
        histogram2_html = pio.to_html(fig2, full_html=False)

        return render_template('histogram_level2.html', histogram_html=histogram2_html)

    except Exception as e:
        return f"Erreur : {str(e)}", 500


@app.route('/histogram/level3')
def histogram_level3():
    try:
        # Charger les données de prévalence par pathologie de niveau 3
        prevalence_by_pathology_level3_df = load_prevalence_by_pathology_level3()

        # Créer l'histogramme de niveau 3 avec des barres horizontales
        fig3 = px.histogram(
            prevalence_by_pathology_level3_df,
            x='Average Prevalence',
            y='Pathology Level 3',
            title='Histogramme de la Prévalence par Pathologie de Niveau 3',
            labels={'Average Prevalence': 'Prévalence Moyenne', 'Pathology Level 3': 'Pathologie'},
            template='plotly_dark',
            orientation='h'  # Barres horizontales
        )
        histogram3_html = pio.to_html(fig3, full_html=False)

        return render_template('histogram_level3.html', histogram_html=histogram3_html)

    except Exception as e:
        return f"Erreur : {str(e)}", 500




# Route principale avec des boutons de navigation
@app.route('/')
def index():
    try:
        return render_template('dashboard.html')
    except Exception as e:
        return f"Erreur : {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
