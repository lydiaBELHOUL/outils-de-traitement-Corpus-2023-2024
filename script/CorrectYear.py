import csv
import re

def fix_years(text):
    """
    Corrige le format des années collées dans le texte en ajoutant une barre oblique entre les années.

    Args:
    text (str): Le texte à corriger.

    Returns:
    str: Le texte avec les années corrigées.
    """
    # Correction des années collées (ex: 19801990 -> 1980/1990)
    text = re.sub(r'(\d{4})(\d{4})', r'\1/\2', text)
    return text

def remove_numbers_in_brackets(text):
    """
    Supprime les chiffres entre crochets dans le texte.

    Args:
    text (str): Le texte à corriger.

    Returns:
    str: Le texte sans les chiffres entre crochets.
    """
    # Suppression des chiffres entre crochets
    text = re.sub(r'\[\d+\]', '', text)
    return text

def correct_csv(input_file, output_file):
    """
    Lit un fichier CSV, corrige le format des années collées dans la colonne 'table',
    supprime les chiffres entre crochets dans la colonne 'context', et écrit le résultat dans un nouveau fichier CSV.

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
            # Corriger la colonne 'table'
            if 'table' in fields:
                row['table'] = fix_years(row['table'])
            
            # Supprimer les chiffres entre crochets dans la colonne 'context'
            if 'context' in fields:
                row['context'] = remove_numbers_in_brackets(row['context'])

            writer.writerow(row)





# Chemins vers les fichiers d'entrée et de sortie
input_file = '/home/lydia/Documents/outil/Bonoutput2AnglaisLowercased.csv'
output_file = '/home/lydia/Documents/outil/Bonoutput2AnglaisLowercasedCorrectYear.csv'

correct_csv(input_file, output_file)


