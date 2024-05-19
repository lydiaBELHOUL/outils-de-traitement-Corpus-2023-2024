import csv
import re
import json

def clean_text(text, remove_parentheses=False):
    """
    Nettoie le texte en supprimant ou en remplaçant des séquences spécifiques.

    Args:
    text (str): Le texte à nettoyer.
    remove_parentheses (bool): Indique s'il faut supprimer le contenu entre parenthèses.

    Returns:
    str: Le texte nettoyé.
    """
    if remove_parentheses:
        # Suppression du contenu entre parenthèses
        text = re.sub(r'\([^)]*\)', '', text)
    # Remplacement des séquences de '\n', '\u200b', et espaces multiples par un espace unique
    text = re.sub(r'[\n\u200b]+', ' ', text)
    # Nettoyage des caractères d'échappement
    text = text.replace("\\'", "'")
    # Suppression des suites de caractères Unicode non imprimables ou spéciaux
    text = re.sub(r'\\x[0-9a-fA-F]{2}', ' ', text)
    # Correction des tirets et guillemets mal encodés
    text = text.replace('â€“', '–').replace('â€™', "'").replace('â€œ', '"').replace('â€', '"')
    # Suppression des espaces multiples
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def clean_json_string(json_string):
    """
    Nettoie une chaîne JSON en supprimant les séquences d'échappement non valides.

    Args:
    json_string (str): La chaîne JSON à nettoyer.

    Returns:
    str: La chaîne JSON nettoyée.
    """
    # Remplacement des séquences d'échappement invalides
    json_string = json_string.replace("\\", "")
    # Correction des guillemets simples et doubles
    json_string = json_string.replace("'", "\"")
    return json_string

def clean_data(input_file, output_file):
    """
    Lit un fichier CSV, nettoie les colonnes 'table' et 'context', et écrit le résultat dans un nouveau fichier CSV.

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
            # Nettoyage de la colonne 'table'
            if 'table' in fields:
                try:
                    table_data = json.loads(clean_json_string(row['table']))
                    table_data['content'] = [clean_text(value, remove_parentheses=True) for value in table_data['content']]
                    row['table'] = json.dumps(table_data)
                except json.JSONDecodeError as e:
                    print(f"Erreur de déserialisation JSON pour la ligne {reader.line_num}: {e}")
                    continue  # Ignorer cette ligne et passer à la suivante
            
            # Nettoyage de la colonne 'context'
            if 'context' in fields:
                row['context'] = clean_text(row['context'])

            writer.writerow(row)

# Chemins vers les fichiers d'entrée et de sortie
input_file = '/home/lydia/Documents/outil/rawAnglais.csv'
output_file = '/home/lydia/Documents/outil/rawAnglaisCleaned.csv'

clean_data(input_file, output_file)
