#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: lydia
verifier si le contenu des lignes est en anglais et ne garder que ces lignes
installer la bibliothèque langdetect 
"""

import csv
import json
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Assurer des résultats reproductibles de détection de langue
DetectorFactory.seed = 0

def is_english(text):
    """
    Détecte si le texte est en anglais.
    
    Args:
    text (str): Le texte à vérifier.
    
    Returns:
    bool: True si le texte est en anglais, False sinon.
    """
    try:
        return detect(text) == 'en'
    except LangDetectException:
        return False

def filter_english_rows(input_file, output_file):
    """
    Filtre les lignes d'un fichier CSV pour ne conserver que celles en anglais.
    
    Args:
    input_file (str): Chemin vers le fichier CSV d'entrée.
    output_file (str): Chemin vers le fichier CSV de sortie.
    """
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            context = row['context']
            if is_english(context):
                writer.writerow(row)

# Chemins vers les fichiers d'entrée et de sortie
input_file = 'raw.csv'
output_file = 'rawAnglais.csv'

# Filtrer les lignes en anglais
filter_english_rows(input_file, output_file)
