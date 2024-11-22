import pandas as pd

# Mapping des colonnes
columns_mapping = {
    "annee": "Year",
    "patho_niv1": "Pathology Level 1",
    "patho_niv2": "Pathology Level 2",
    "patho_niv3": "Pathology Level 3",
    "top": "Topology",
    "cla_age_5": "Age Group (5 years)",
    "sexe": "Gender",
    "region": "Region",
    "dept": "Department",
    "Ntop": "Patient Count (top)",
    "Npop": "Total Population",
    "prev": "Prevalence",
    "Niveau prioritaire": "Priority Level",
    "libelle_classe_age": "Age Group Label",
    "libelle_sexe": "Gender Label",
    "tri": "Sorting"
}

raw_file_path = "../../raw_data.csv"
staged_file_path = "../../staged_data.csv"

# Lire le fichier avec l'encodage UTF-8
print(f"Reading raw file from: {raw_file_path}")
dtype_dict = {
    "Year": str,  # Année sous forme de chaîne (exemple : "2024")
    "Pathology Level 1": str,  # Niveau 1 des pathologies, chaîne de texte
    "Pathology Level 2": str,  # Niveau 2 des pathologies, chaîne de texte
    "Pathology Level 3": str,  # Niveau 3 des pathologies, chaîne de texte
    "Topology": str,  # Chaîne, probablement catégorielle
    "Age Group (5 years)": str,  # Groupe d'âge sous forme de chaîne (ex. : "0-4", "5-9")
    "Gender": str,  # Sexe, chaîne (ex. : "Male", "Female")
    "Region": str,  # Région géographique, chaîne
    "Department": str,  # Département géographique, chaîne
    "Patient Count (top)": int,  # Nombre de patients, entier
    "Total Population": int,  # Population totale, entier
    "Prevalence": float,  # Prévalence, nombre à virgule flottante
    "Priority Level": str,  # Niveau de priorité, chaîne ou peut-être une catégorie
    "Age Group Label": str,  # Étiquette du groupe d'âge, chaîne
    "Gender Label": str,  # Étiquette du sexe, chaîne
    "Sorting": int  # Ordre de tri, entier
}

raw_file = pd.read_csv(
    raw_file_path, 
    sep=";", 
    header=0, 
    skipinitialspace=True, 
    encoding='utf-8',
    dtype=dtype_dict
)

raw_file = pd.read_csv(raw_file_path, sep=";", header=0, skipinitialspace=True, encoding='utf-8')  # Lecture en UTF-8

# Renommer les colonnes selon le nouveau schéma
print('Renaming columns in the raw data')
renamed_columns = raw_file.rename(columns=columns_mapping)

# Nettoyage des données
print("Cleaning data (trimming spaces and correcting formats)")
# Suppression des espaces en début et fin des chaînes dans les colonnes de texte
renamed_columns = renamed_columns.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Conversion des colonnes numériques nécessaires
numeric_columns = ["Patient Count (top)", "Total Population", "Prevalence", "Sorting"]
for col in numeric_columns:
    renamed_columns[col] = pd.to_numeric(renamed_columns[col], errors='coerce')

# Enregistrement des données nettoyées dans le fichier de staging
print(f'Writing transformed data to: {staged_file_path}')
renamed_columns.to_csv(staged_file_path, sep=",", index=False, encoding="utf-8-sig")  # Sauvegarde en UTF-8-sig

print('Data successfully written.')
