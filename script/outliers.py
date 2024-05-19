#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce script traite un jeu de données en tokenisant le texte dans la colonne 'context',
en calculant le nombre de tokens pour chaque contexte, en filtrant les valeurs aberrantes 
basées sur l'intervalle interquartile (IQR), et en affichant et en sauvegardant les données filtrées.

Auteur: Lydia
"""

import pandas as pd
import json  # Importé mais non utilisé dans ce script
from nltk.tokenize import word_tokenize
from nltk import download
from prettytable import PrettyTable

# Télécharger les modèles de tokenisation Punkt de NLTK
download('punkt')

def calculate_token_counts(data):
    """
    Calculer le nombre de tokens dans la colonne 'context' pour chaque ligne du DataFrame.
    
    Paramètres:
    data (pd.DataFrame): Le DataFrame d'entrée contenant une colonne 'context'.
    
    Retourne:
    List[int]: Une liste contenant le nombre de tokens pour chaque contexte.
    """
    tokens_per_context = []  # Liste pour stocker le nombre de tokens par contexte

    for _, row in data.iterrows():
        try:
            # Tokeniser le contexte entier
            tokens_context = word_tokenize(row['context'])
            tokens_per_context.append(len(tokens_context))
        except Exception as e:
            print(f"Erreur lors de la tokenisation: {e}")

    return tokens_per_context

# Charger les données
data = pd.read_csv('/home/lydia/Documents/outil/Bonoutput2Validated.csv')

# Calculer le nombre de tokens pour chaque contexte
data['tokens_per_context'] = calculate_token_counts(data)

# Calculer l'IQR pour filtrer les valeurs aberrantes
Q1 = data['tokens_per_context'].quantile(0.25)
Q3 = data['tokens_per_context'].quantile(0.75)
IQR = Q3 - Q1
borne_inf = Q1 - 1.5 * IQR
borne_sup = Q3 + 1.5 * IQR

# Filtrer les données pour éliminer les valeurs aberrantes
filtered_data = data[(data['tokens_per_context'] >= borne_inf) & (data['tokens_per_context'] <= borne_sup)]

# Afficher les statistiques en utilisant PrettyTable
table = PrettyTable()
table.field_names = ["Description", "Nombre"]
table.add_row(["Nombre de contextes initial", len(data)])
table.add_row(["Nombre de contextes après filtration", len(filtered_data)])

print(table)

# Optionnel : sauvegarder les données filtrées
filtered_data.to_csv('/home/lydia/Documents/outil/outliers.csv', index=False)
print("Les données filtrées ont été enregistrées.")
