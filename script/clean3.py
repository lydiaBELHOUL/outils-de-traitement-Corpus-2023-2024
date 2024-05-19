#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ce script a pour fonction la supprission des lignes spécifiques qui contiennent des caractères
qui n'ont pas lieu d'etre malgré deux nettoyage 
@author: lydia
"""
import csv
import re

def contains_invalid_sequences(text):
    """
    Vérifie si le texte contient des séquences non valides.

    Args:
    text (str): Le texte à vérifier.

    Returns:
    bool: True si le texte contient des séquences non valides, False sinon.
    """
    invalid_patterns = [
        r'\xa0',              # Espaces insécables
        r'\u200b\u200b',      # Espaces zéro largeur
        r'\d+\s*\xa0\s*ft',   # Mesures avec \xa0
        r'\d+\s*\xa0\s*in',   # Mesures avec \xa0
        r'\xa0',              # Espaces insécables isolés ou entre des caractères
        r'\u200b',            # Espaces zéro largeur isolés ou entre des caractères
        r'\\u[0-9a-fA-F]{2,4}',# Séquences Unicode
        r'\xa0',              # Espaces insécables
        r'\u200b\u200b',      # Espaces zéro largeur
        r'\\u[0-9a-fA-F]{2,4}', # Séquences Unicode
        r'\d+\s*\xa0\s*ft',   # Mesures avec \xa0
        r'\d+\s*\xa0\s*in',   # Mesures avec \xa0
        r'\xa0',              # Espaces insécables isolés ou entre des caractères
        r'\\u[0-9a-fA-F]{2,4}',# Séquences Unicode
        r'(?<=\S)\xa0(?=\S)', # \xa0 entre deux caractères non espaces
       r'(?<=\S)\u200b(?=\S)',# \u200b entre deux caractères non espaces
       r'\xa0',                       # Espaces insécables
        r'\u200b\u200b',               # Espaces zéro largeur
        r'\\u[0-9a-fA-F]{2,4}',        # Séquences Unicode
        r'\d+\s*\xa0\s*ft',            # Mesures avec \xa0
        r'\d+\s*\xa0\s*in',            # Mesures avec \xa0
        r'(?<=\S)\xa0(?=\S)',          # \xa0 entre deux caractères non espaces
        r'(?<=\S)\u200b(?=\S)',        # \u200b entre deux caractères non espaces
        r'(?<=\S)\\u[0-9a-fA-F]{2,4}(?=\S)', # Séquences Unicode entre caractères non espaces
        r'\s+\xa0\s+',                 # \xa0 entouré par des espaces
        r'\s+\u200b\s+'                # \u200b entouré par des espaces
    ]
    for pattern in invalid_patterns:
        if re.search(pattern, text):
            return True
    return False

def filter_invalid_lines(input_file, output_file):
    """
    Lit un fichier CSV, filtre les lignes contenant des séquences non valides, et écrit le résultat dans un nouveau fichier CSV.

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
            table_valid = True
            context_valid = True

            # Vérifier la colonne 'table'
            if 'table' in fields:
                table_text = row['table']
                if contains_invalid_sequences(table_text):
                    table_valid = False
            
            # Vérifier la colonne 'context'
            if 'context' in fields:
                context_text = row['context']
                if contains_invalid_sequences(context_text):
                    context_valid = False
            
            # Écrire la ligne uniquement si elle est valide
            if table_valid and context_valid:
                writer.writerow(row)

# Chemins vers les fichiers d'entrée et de sortie
input_file = '/home/lydia/Documents/outil/Bonoutput2AnglaisCleaned2.csv'
output_file = '/home/lydia/Documents/outil/Bonoutput2AnglaisFiltered.csv'

filter_invalid_lines(input_file, output_file)
