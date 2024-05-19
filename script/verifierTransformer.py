import json
import pandas as pd
from datasets import Dataset
'''
TP3 vérifier le format du corpus et transformer en Dataset
'''
def validate_and_transform(input_file, output_file):
    # Charger le fichier CSV
    df = pd.read_csv(input_file)
    
    # Vérification de la structure et transformation en Dataset
    valid_data = []
    
    for index, row in df.iterrows():
        try:
            table_text = json.loads(row['table'].replace("'", "\""))
            context_text = row['context']
            
            if 'column_header' in table_text and 'row_number' in table_text and 'content' in table_text:
                column_header = table_text['column_header']
                row_number = table_text['row_number']
                content = table_text['content']
                
                if (isinstance(column_header, list) and isinstance(row_number, list) and isinstance(content, list) and isinstance(context_text, str)):
                    valid_data.append({
                        "table": table_text,
                        "context": context_text
                    })
        
        except json.JSONDecodeError as e:
            print(f"Erreur de déserialisation JSON pour la ligne {index + 1}: {e}")
    
    # Créer le DataFrame à partir des données valides
    valid_df = pd.DataFrame(valid_data)
    
    # Convertir en Dataset Hugging Face
    dataset = Dataset.from_pandas(valid_df)
    
    # Sauvegarder le nouveau fichier CSV nettoyé
    valid_df.to_csv(output_file, index=False)
    
    return dataset

# Chemins vers les fichiers d'entrée et de sortie
input_file = '/home/lydia/Documents/outil/Bonoutput2AnglaisLowercasedCorrectYear.csv'
output_file = '/home/lydia/Documents/outil/Bonoutput2Validated.csv'

# Lancer la validation et la transformation
dataset = validate_and_transform(input_file, output_file)

# Afficher quelques exemples du Dataset
print(dataset)
