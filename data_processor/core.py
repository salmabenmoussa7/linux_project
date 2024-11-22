import pandas as pd

# Charger les données du fichier staged_data.csv
print("Loading staged data...")
staged_data = pd.read_csv("../staged_data.csv", sep=",", header=0, skipinitialspace=True)

# Calculer des indicateurs simples
print("Calculating simple indicators...")

# Total des patients
total_patients = staged_data["Patient Count (top)"].sum()

# Prévalence moyenne
average_prevalence = staged_data["Prevalence"].mean()

# Médiane de la prévalence
median_prevalence = staged_data["Prevalence"].median()

# Nombre de pathologies uniques (niveau 1)
unique_pathologies_level1 = staged_data["Pathology Level 1"].nunique()

# Nombre de pathologies uniques (niveau 2)
unique_pathologies_level2 = staged_data["Pathology Level 2"].nunique()

# Nombre de pathologies uniques (niveau 3)
unique_pathologies_level3 = staged_data["Pathology Level 3"].nunique()

# Répartition des patients par région
patients_by_region = staged_data.groupby("Region")["Patient Count (top)"].sum()

# Répartition des patients par département
patients_by_department = staged_data.groupby("Department")["Patient Count (top)"].sum()

# Calcul des prévalences moyennes par sexe et par année
prevalence_by_gender_year = staged_data.groupby(["Year", "Gender"])["Prevalence"].mean()

# Distribution des prévalences pour chaque pathologie (niveau 1, 2 et 3)
prevalence_by_pathology_level1 = staged_data.groupby("Pathology Level 1")["Prevalence"].mean()
prevalence_by_pathology_level2 = staged_data.groupby("Pathology Level 2")["Prevalence"].mean()
prevalence_by_pathology_level3 = staged_data.groupby("Pathology Level 3")["Prevalence"].mean()

# Évolution de la prévalence au fil du temps (année par année)
prevalence_by_year = staged_data.groupby("Year")["Prevalence"].mean()

# Créer un DataFrame des Indicateurs de Base
base_indicators_df = pd.DataFrame({
    "Indicator": ["Total Patients", "Average Prevalence", "Median Prevalence", 
                  "Unique Pathologies Level 1", "Unique Pathologies Level 2", "Unique Pathologies Level 3"],
    "Value": [total_patients, average_prevalence, median_prevalence,
              unique_pathologies_level1, unique_pathologies_level2, unique_pathologies_level3]
})

# Créer un DataFrame des Répartitions
# Répartition des patients par région
patients_by_region_df = pd.DataFrame(patients_by_region).reset_index()
patients_by_region_df.columns = ["Region", "Patient Count"]


# Dictionnaire des codes région avec leurs noms
region_names = {
    1: "Île-de-France",
    2: "Champagne-Ardenne",
    3: "Haute-Normandie",
    4: "Bretagne",
    6: "Poitou-Charentes",
    11: "Rhône-Alpes",
    24: "Nouvelle-Aquitaine",
    27: "Languedoc-Roussillon",
    28: "Midi-Pyrénées",
    32: "Rhône-Alpes",
    44: "Provence-Alpes-Côte d'Azur",
    52: "Alsace",
    53: "Lorraine",
    75: "Île-de-France (Paris)",
    76: "Haute-Normandie",
    84: "Provence-Alpes-Côte d'Azur",
    93: "Rhône-Alpes",
    94: "Alsace",
    99: "Non renseigné / Collectivités d'Outre-Mer"
}


# Dictionnaires de latitudes et longitudes pour chaque région de France

latitudes = {
    "Île-de-France": 48.8566,
    "Champagne-Ardenne": 49.0,
    "Haute-Normandie": 49.4,
    "Bretagne": 48.6,
    "Poitou-Charentes": 46.5,
    "Rhône-Alpes": 45.7,
    "Nouvelle-Aquitaine": 44.0,
    "Languedoc-Roussillon": 43.5,
    "Midi-Pyrénées": 43.5,
    "Provence-Alpes-Côte d'Azur": 43.5,
    "Alsace": 48.5,
    "Lorraine": 48.7,
    "Île-de-France (Paris)": 48.8566,
    "Haute-Normandie (again)": 49.4,
    "Provence-Alpes-Côte d'Azur (again)": 43.5,
    "Rhône-Alpes (again)": 45.7,
    "Alsace (again)": 48.5,
    "Non renseigné / Collectivités d'Outre-Mer": None  # Pas de coordonnées fixes
}

longitudes = {
    "Île-de-France": 2.3522,
    "Champagne-Ardenne": 4.0,
    "Haute-Normandie": 1.1,
    "Bretagne": -2.0,
    "Poitou-Charentes": -0.5,
    "Rhône-Alpes": 4.9,
    "Nouvelle-Aquitaine": -0.5,
    "Languedoc-Roussillon": 3.5,
    "Midi-Pyrénées": 1.5,
    "Provence-Alpes-Côte d'Azur": 6.0,
    "Alsace": 7.5,
    "Lorraine": 6.2,
    "Île-de-France (Paris)": 2.3522,
    "Haute-Normandie (again)": 1.1,
    "Provence-Alpes-Côte d'Azur (again)": 6.0,
    "Rhône-Alpes (again)": 4.9,
    "Alsace (again)": 7.5,
    "Non renseigné / Collectivités d'Outre-Mer": None  # Pas de coordonnées fixes
}


# Ajouter une colonne 'Region Name' en utilisant le dictionnaire des noms des régions
patients_by_region_df['Region Name'] = patients_by_region_df['Region'].map(region_names)
patients_by_region_df['Latitude'] = patients_by_region_df['Region Name'].map(latitudes)
patients_by_region_df['Longitude'] = patients_by_region_df['Region Name'].map(longitudes)

# Répartition des patients par département
patients_by_department_df = pd.DataFrame(patients_by_department).reset_index()
patients_by_department_df.columns = ["Department", "Patient Count"]


# Création d'un dictionnaire pour les départements français
department_names = {
    "01": "Ain",
    "02": "Aisne",
    "03": "Allier",
    "04": "Alpes-de-Haute-Provence",
    "05": "Hautes-Alpes",
    "06": "Alpes-Maritimes",
    "07": "Ardèche",
    "08": "Ardennes",
    "09": "Ariège",
    "10": "Aube",
    "11": "Aude",
    "12": "Aveyron",
    "13": "Bouches-du-Rhône",
    "14": "Calvados",
    "15": "Cantal",
    "16": "Charente",
    "17": "Charente-Maritime",
    "18": "Cher",
    "19": "Corrèze",
    "2A": "Corse-du-Sud",
    "2B": "Haute-Corse",
    "21": "Côte-d'Or",
    "22": "Côtes-d'Armor",
    "23": "Creuse",
    "24": "Dordogne",
    "25": "Doubs",
    "26": "Drôme",
    "27": "Eure",
    "28": "Eure-et-Loir",
    "29": "Finistère",
    "30": "Gard",
    "31": "Haute-Garonne",
    "32": "Gers",
    "33": "Gironde",
    "34": "Hérault",
    "35": "Ille-et-Vilaine",
    "36": "Indre",
    "37": "Indre-et-Loire",
    "38": "Isère",
    "39": "Jura",
    "40": "Landes",
    "41": "Loir-et-Cher",
    "42": "Loire",
    "43": "Haute-Loire",
    "44": "Loire-Atlantique",
    "45": "Loiret",
    "46": "Lot",
    "47": "Lot-et-Garonne",
    "48": "Lozère",
    "49": "Maine-et-Loire",
    "50": "Manche",
    "51": "Marne",
    "52": "Haute-Marne",
    "53": "Mayenne",
    "54": "Meurthe-et-Moselle",
    "55": "Meuse",
    "56": "Morbihan",
    "57": "Moselle",
    "58": "Nièvre",
    "59": "Nord",
    "60": "Oise",
    "61": "Orne",
    "62": "Pas-de-Calais",
    "63": "Puy-de-Dôme",
    "64": "Pyrénées-Atlantiques",
    "65": "Hautes-Pyrénées",
    "66": "Pyrénées-Orientales",
    "67": "Bas-Rhin",
    "68": "Haut-Rhin",
    "69": "Rhône",
    "70": "Haute-Saône",
    "71": "Saône-et-Loire",
    "72": "Sarthe",
    "73": "Savoie",
    "74": "Haute-Savoie",
    "75": "Paris",
    "76": "Seine-Maritime",
    "77": "Seine-et-Marne",
    "78": "Yvelines",
    "79": "Deux-Sèvres",
    "80": "Somme",
    "81": "Tarn",
    "82": "Tarn-et-Garonne",
    "83": "Var",
    "84": "Vaucluse",
    "85": "Vendée",
    "86": "Vienne",
    "87": "Haute-Vienne",
    "88": "Vosges",
    "89": "Yonne",
    "90": "Territoire de Belfort",
    "91": "Essonne",
    "92": "Hauts-de-Seine",
    "93": "Seine-Saint-Denis",
    "94": "Val-de-Marne",
    "95": "Val-d'Oise",
    "971": "Guadeloupe",
    "972": "Martinique",
    "973": "Guyane",
    "974": "La Réunion",
    "976": "Mayotte",
    "999": "Hors France Métropolitaine"
}

# Ajouter une colonne 'Department Name' en utilisant le dictionnaire des noms des départements
patients_by_department_df['Department Name'] = patients_by_department_df['Department'].map(department_names)

# Répartition des prévalences par sexe et année
prevalence_by_gender_year_df = pd.DataFrame(prevalence_by_gender_year).reset_index()
prevalence_by_gender_year_df.columns = ["Year", "Gender", "Average Prevalence"]

genders = {
    1 : "Homme",
    2 : "Femme",
    9 : "Tous sexes" 
}

# Ajouter une colonne 'Department Name' en utilisant le dictionnaire des noms des départements
prevalence_by_gender_year_df['Gender Label'] = prevalence_by_gender_year_df['Gender'].map(genders)

# Répartition des prévalences par pathologie (niveau 1)
prevalence_by_pathology_level1_df = pd.DataFrame(prevalence_by_pathology_level1).reset_index()
prevalence_by_pathology_level1_df.columns = ["Pathology Level 1", "Average Prevalence"]

pathologies_level1_short_names = {
    "Maladies cardioneurovasculaires": "Cardio-neurovasc.",
    "Cancers": "Cancers",
    "Maladies inflammatoires ou rares ou infection VIH": "Inflamm./rares/VIH",
    "Maladies neurologiques": "Neurologiques",
    "Maladies psychiatriques": "Psychiatriques",
    "Traitements psychotropes (hors pathologies)": "Psychotropes",
    "Insuffisance rénale chronique terminale": "Insuff. rénale",
    "Traitements du risque vasculaire (hors pathologies)": "Risque vasculaire",
    "Affections de longue durée (dont 31 et 32) pour d'autres causes": "ALD autres causes",
    "Diabète": "Diabète",
    "Hospitalisation pour Covid-19": "Covid-19",
    "Hospitalisations hors pathologies repérées (avec ou sans pathologies, traitements ou maternité)": "Hospit. hors pathologies",
    "Maladies du foie ou du pancréas (hors mucoviscidose)": "Foie/pancréas",
    "Maladies respiratoires chroniques (hors mucoviscidose)": "Respiratoires chroniques",
    "Pas de pathologie repérée, traitement, maternité, hospitalisation ou traitement antalgique ou anti-inflammatoire": "Aucune pathologie",
    "Total consommants tous régimes": "Total consommateurs",
    "Traitement antalgique ou anti-inflammatoire (hors pathologies, traitements, maternité ou hospitalisations)": "Antalgiques/anti-inflam.",
    "Maternité (avec ou sans pathologies)": "Maternité"
}

# Ajouter une colonne 'Pathology Name' en utilisant le dictionnaire des noms des pathologies
prevalence_by_pathology_level1_df['Pathology Name'] = prevalence_by_pathology_level1_df['Pathology Level 1'].map(pathologies_level1_short_names)

# Répartition des prévalences par pathologie (niveau 2)
prevalence_by_pathology_level2_df = pd.DataFrame(prevalence_by_pathology_level2).reset_index()
prevalence_by_pathology_level2_df.columns = ["Pathology Level 2", "Average Prevalence"]


pathologies_level2_short_names = {
    "Maladies inflammatoires chroniques": "Inflamm. chroniques",
    "Maladies rares": "Rares",
    "Accident vasculaire cérébral": "AVC",
    "Autres cancers": "Autres cancers",
    "Cancer bronchopulmonaire": "Cancer pulmonaire",
    "Cancer colorectal": "Cancer colorectal",
    "Insuffisance cardiaque": "Insuff. cardiaque",
    "Maladie coronaire": "Coronaires",
    "Cancer de la prostate": "Cancer prostate",
    "Cancer du sein de la femme": "Cancer sein (F)",
    "Affections de longue durée (dont 31 et 32) pour d'autres causes": "ALD autres causes",
    "Artériopathie périphérique": "Artériopathie",
    "Autres affections cardiovasculaires": "Autres cardio.",
    "Autres affections neurologiques": "Autres neuro.",
    "Autres troubles psychiatriques": "Autres psychiat.",
    "Diabète": "Diabète",
    "Dialyse chronique": "Dialyse",
    "Déficience mentale": "Déficience mentale",
    "Démences (dont maladie d'Alzheimer)": "Démences/Alzheimer",
    "Embolie pulmonaire": "Embolie pulmonaire",
    "Hospitalisation pour Covid-19": "Covid-19",
    "Hospitalisations hors pathologies repérées (avec ou sans pathologies, traitements ou maternité)": "Hospit. hors pathologies",
    "Infection par le VIH": "VIH",
    "Lésion médullaire": "Lésion médullaire",
    "Maladie de Parkinson": "Parkinson",
    "Maladie valvulaire": "Valvulopathies",
    "Maladies du foie ou du pancréas (hors mucoviscidose)": "Foie/pancréas",
    "Maladies respiratoires chroniques (hors mucoviscidose)": "Respir. chroniques",
    "Myopathie ou myasthénie": "Myopathies",
    "Pas de pathologie repérée, traitement, maternité, hospitalisation ou traitement antalgique ou anti-inflammatoire": "Aucune pathologie",
    "Sclérose en plaques": "Sclérose en plaques",
    "Suivi de transplantation rénale": "Suivi transpl. rénale",
    "Total consommants tous régimes": "Total consommateurs",
    "Traitement antalgique ou anti-inflammatoire (hors pathologies, traitements, maternité ou hospitalisations)": "Antalgiques/anti-inflam.",
    "Traitements antidépresseurs ou régulateurs de l'humeur (hors pathologies)": "Antidépresseurs",
    "Traitements antihypertenseurs (hors pathologies)": "Antihypertenseurs",
    "Traitements anxiolytiques (hors pathologies)": "Anxiolytiques",
    "Traitements hypnotiques (hors pathologies)": "Hypnotiques",
    "Traitements hypolipémiants (hors pathologies)": "Hypolipémiants",
    "Traitements neuroleptiques (hors pathologies)": "Neuroleptiques",
    "Transplantation rénale": "Transpl. rénale",
    "Troubles addictifs": "Addictions",
    "Troubles du rythme ou de la conduction cardiaque": "Rythme/conduction card.",
    "Troubles névrotiques et de l'humeur": "Névroses/humeur",
    "Troubles psychiatriques débutant dans l'enfance": "Psychiatrie enfant",
    "Troubles psychotiques": "Psychotiques",
    "Épilepsie": "Épilepsie",
    "Maternité (avec ou sans pathologies)": "Maternité"
}

# Ajouter une colonne 'Pathology Name' en utilisant le dictionnaire des noms des pathologies
prevalence_by_pathology_level2_df['Pathology Name'] = prevalence_by_pathology_level2_df['Pathology Level 2'].map(pathologies_level2_short_names)


# Répartition des prévalences par pathologie (niveau 3)
prevalence_by_pathology_level3_df = pd.DataFrame(prevalence_by_pathology_level3).reset_index()
prevalence_by_pathology_level3_df.columns = ["Pathology Level 3", "Average Prevalence"]


pathologies_level3_short_names = {
    "Accident vasculaire cérébral aigu": "AVC aigu",
    "Affections de longue durée (dont 31 et 32) pour d'autres causes": "ALD autres causes",
    "Artériopathie périphérique": "Artériopathie",
    "Autres affections cardiovasculaires": "Autres cardio.",
    "Autres affections neurologiques": "Autres neuro.",
    "Autres cancers actifs": "Cancers actifs (autres)",
    "Autres cancers sous surveillance": "Cancers sous surv. (autres)",
    "Autres maladies inflammatoires chroniques": "Inflamm. chroniques (autres)",
    "Autres troubles psychiatriques": "Psychiatrie (autres)",
    "Cancer bronchopulmonaire actif": "Cancer pulmonaire actif",
    "Cancer bronchopulmonaire sous surveillance": "Cancer pulm. sous surv.",
    "Cancer colorectal actif": "Cancer colorectal actif",
    "Cancer colorectal sous surveillance": "Cancer colorectal sous surv.",
    "Diabète": "Diabète",
    "Dialyse chronique": "Dialyse",
    "Déficience mentale": "Déficience mentale",
    "Démences (dont maladie d'Alzheimer)": "Démences/Alzheimer",
    "Embolie pulmonaire": "Embolie pulmonaire",
    "Hospitalisation pour Covid-19": "Covid-19",
    "Hospitalisations hors pathologies repérées (avec ou sans pathologies, traitements ou maternité)": "Hospit. hors pathologies",
    "Hémophilie ou troubles de l'hémostase graves": "Hémophilie",
    "Infection par le VIH": "VIH",
    "Insuffisance cardiaque aiguë": "Insuff. cardiaque aiguë",
    "Insuffisance cardiaque chronique": "Insuff. cardiaque chronique",
    "Lésion médullaire": "Lésion médullaire",
    "Maladie coronaire chronique": "Coronaires chroniques",
    "Maladie de Parkinson": "Parkinson",
    "Maladie valvulaire": "Valvulopathies",
    "Maladies du foie ou du pancréas (hors mucoviscidose)": "Foie/pancréas",
    "Maladies inflammatoires chroniques intestinales": "Inflamm. chroniques intest.",
    "Maladies métaboliques héréditaires ou amylose": "Métabolique/amylose",
    "Maladies respiratoires chroniques (hors mucoviscidose)": "Respir. chroniques",
    "Mucoviscidose": "Mucoviscidose",
    "Myopathie ou myasthénie": "Myopathies",
    "Pas de pathologie repérée, traitement, maternité, hospitalisation ou traitement antalgique ou anti-inflammatoire": "Aucune pathologie",
    "Polyarthrite rhumatoïde ou maladies apparentées": "Polyarthrite",
    "Sclérose en plaques": "Sclérose en plaques",
    "Spondylarthrite ankylosante ou maladies apparentées": "Spondylarthrite",
    "Suivi de transplantation rénale": "Suivi transpl. rénale",
    "Syndrome coronaire aigu": "Syndrome coron. aigu",
    "Séquelle d'accident vasculaire cérébral": "Séquelle AVC",
    "Total consommants tous régimes": "Total consommateurs",
    "Traitement antalgique ou anti-inflammatoire (hors pathologies, traitements, maternité ou hospitalisations)": "Antalgiques/anti-inflam.",
    "Traitements antidépresseurs ou régulateurs de l'humeur (hors pathologies)": "Antidépresseurs",
    "Traitements antihypertenseurs (hors pathologies)": "Antihypertenseurs",
    "Traitements anxiolytiques (hors pathologies)": "Anxiolytiques",
    "Traitements hypnotiques (hors pathologies)": "Hypnotiques",
    "Traitements hypolipémiants (hors pathologies)": "Hypolipémiants",
    "Traitements neuroleptiques (hors pathologies)": "Neuroleptiques",
    "Transplantation rénale": "Transpl. rénale",
    "Troubles addictifs": "Addictions",
    "Troubles du rythme ou de la conduction cardiaque": "Rythme/conduction card.",
    "Troubles névrotiques et de l'humeur": "Névroses/humeur",
    "Troubles psychiatriques débutant dans l'enfance": "Psychiatrie enfant",
    "Troubles psychotiques": "Psychotiques",
    "Épilepsie": "Épilepsie",
    "Cancer de la prostate actif": "Cancer prostate actif",
    "Cancer de la prostate sous surveillance": "Cancer prostate sous surv.",
    "Cancer du sein de la femme actif": "Cancer sein (F) actif",
    "Cancer du sein de la femme sous surveillance": "Cancer sein (F) sous surv.",
    "Maternité (avec ou sans pathologies)": "Maternité"
}

# Ajouter une colonne 'Pathology Name' en utilisant le dictionnaire des noms des pathologies
prevalence_by_pathology_level3_df['Pathology Name'] = prevalence_by_pathology_level3_df['Pathology Level 3'].map(pathologies_level3_short_names)


# Créer un DataFrame de l'Évolution au Fil du Temps
prevalence_by_year_df = pd.DataFrame(prevalence_by_year).reset_index()
prevalence_by_year_df.columns = ["Year", "Average Prevalence"]

# Sauvegarder tous les DataFrames dans des fichiers CSV distincts
base_indicators_df.to_csv("../base_indicators.csv", index=False, encoding="utf-8")
patients_by_region_df.to_csv("../patients_by_region.csv", index=False, encoding="utf-8")
patients_by_department_df.to_csv("../patients_by_department.csv", index=False, encoding="utf-8")
prevalence_by_gender_year_df.to_csv("../prevalence_by_gender_year.csv", index=False, encoding="utf-8")
prevalence_by_pathology_level1_df.to_csv("../prevalence_by_pathology_level1.csv", index=False, encoding="utf-8")
prevalence_by_pathology_level2_df.to_csv("../prevalence_by_pathology_level2.csv", index=False, encoding="utf-8")
prevalence_by_pathology_level3_df.to_csv("../prevalence_by_pathology_level3.csv", index=False, encoding="utf-8")
prevalence_by_year_df.to_csv("../prevalence_by_year.csv", index=False, encoding="utf-8")

print("DataFrames saved as separate CSV files.")

