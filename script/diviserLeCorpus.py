#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Script pour diviser un corpus en ensembles d'entraînement et de test.

Ce script lit un fichier CSV contenant un corpus, le divise en un ensemble
d'entraînement (80%) et un ensemble de test (20%), et sauvegarde les résultats
dans de nouveaux fichiers CSV.

Utilisation:
    python split_dataset.py

Dépendances:
    pandas, scikit-learn

"""

import pandas as pd
from sklearn.model_selection import train_test_split

# Charger les données
data = pd.read_csv('/chemin/vers/votre/Bonoutput2Validated.csv')  # Mettez à jour le chemin vers votre fichier CSV

# Diviser les données en ensembles d'entraînement et de test
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Sauvegarder les ensembles d'entraînement et de test dans de nouveaux fichiers CSV
train_data.to_csv('/chemin/vers/votre/train_data.csv', index=False)
test_data.to_csv('/chemin/vers/votre/test_data.csv', index=False)

print("Les ensembles de données d'entraînement et de test ont été créés et sauvegardés.")
