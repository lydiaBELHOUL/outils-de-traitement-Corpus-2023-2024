#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lowercase.py pour transformer les caractères en minuscules

@author: lydia
"""

import csv

def lowercase_text(text):
    """
    Transforme toutes les majuscules en minuscules dans le texte.

    Args:
    text (str): Le texte à transformer.

    Returns:
    str: Le texte transformé en minuscules.
    """
    return text.lower()

def transform_to_lowercase(input_file, output_file):
    """
    Lit un fichier CSV, transforme toutes les majuscules en minuscules, et écrit le résultat dans un nouveau fichier CSV.

    Args:
    input_file (str): Chemin vers le fichier CSV d'entrée.
    output_file (str): Chemin vers le fichier CSV de sortie.
    """
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fields = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fields)
        writer.writeheader()
        
        for row in reader:
            # Transformer la colonne 'table' en minuscules
            if 'table' in fields:
                row['table'] = lowercase_text(row['table'])
            
            # Transformer la colonne 'context' en minuscules
            if 'context' in fields:
                row['context'] = lowercase_text(row['context'])

            writer.writerow(row)

# Chemins vers les fichiers d'entrée et de sortie
input_file = '/home/lydia/Documents/outil/Bonoutput2AnglaisFiltered.csv'
output_file = '/home/lydia/Documents/outil/Bonoutput2AnglaisLowercased.csv'

transform_to_lowercase(input_file, output_file)
