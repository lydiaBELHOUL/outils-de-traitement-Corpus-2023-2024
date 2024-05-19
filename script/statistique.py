import pandas as pd
import json
from nltk.tokenize import word_tokenize
from nltk import download
from prettytable import PrettyTable
'''
faire les statistiques j'ai choisis de calculer la moyenne des token de la table , la moyenne des tocken 
de la phrase1, et la moyenne des tockens du paragraphe
afficher en format de tableau 
visualistaion des résultat en plot'
'''

# Assurez-vous que le tokenizer NLTK est téléchargé.
download('punkt')

def calculate_token_counts(data):
    tokens_per_table = []
    tokens_per_first_sentence = []
    tokens_per_context = []  # Ajout pour le calcul total des tokens par contexte

    for _, row in data.iterrows():
        try:
            # Extraire et tokeniser le contenu du tableau
            table_content = " ".join([item for sublist in json.loads(row['table'].replace("'", "\""))['content'] for item in sublist])
            tokens_table = word_tokenize(table_content)
            tokens_per_table.append(len(tokens_table))

            # Extraire et tokeniser la première phrase du contexte
            first_sentence = row['context'].split('.')[0]
            tokens_context_first_sentence = word_tokenize(first_sentence)
            tokens_per_first_sentence.append(len(tokens_context_first_sentence))

            # Extraire et tokeniser le contexte entier
            tokens_context = word_tokenize(row['context'])
            tokens_per_context.append(len(tokens_context))
        except json.JSONDecodeError:
            print("Erreur de décodage JSON dans les données, vérifiez le format du tableau")

    return tokens_per_table, tokens_per_first_sentence, tokens_per_context

# Charger les données
data = pd.read_csv('/home/lydia/Documents/outil/Bonoutput2Validated.csv')  # Assurez-vous que le chemin est correct

# Calculer les statistiques
tokens_table, tokens_first_sentence, tokens_context = calculate_token_counts(data)

# Calcul des moyennes
average_tokens_table = sum(tokens_table) / len(tokens_table) if tokens_table else 0
average_tokens_first_sentence = sum(tokens_first_sentence) / len(tokens_first_sentence) if tokens_first_sentence else 0
average_tokens_context = sum(tokens_context) / len(tokens_context) if tokens_context else 0

# Préparer le tableau pour l'affichage
table = PrettyTable()
table.field_names = ["Description", "Moyenne"]
table.add_row(["Moyenne des tokens par tableau", f"{average_tokens_table:.2f}"])
table.add_row(["Moyenne des tokens par première phrase", f"{average_tokens_first_sentence:.2f}"])
table.add_row(["Moyenne des tokens par contexte", f"{average_tokens_context:.2f}"])  # Affichage de la moyenne des tokens par contexte

# Afficher le tableau
print(table) 


# ajouter la visualisation des résultats 

import matplotlib.pyplot as plt

# Noms des métriques
metrics = ['Tokens par tableau', 'Tokens par première phrase', 'Tokens par contexte']

# Valeurs moyennes calculées
values = [average_tokens_table, average_tokens_first_sentence, average_tokens_context]
#visualistaion des résultats

plt.figure(figsize=(10, 5))
plt.bar(metrics, values, color=['blue', 'green', 'red'])
plt.xlabel('Métriques')
plt.ylabel('Nombre moyen de tokens')
plt.title('Comparaison du nombre moyen de tokens')
plt.show()
