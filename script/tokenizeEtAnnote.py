#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TP3 tockeniser et annoter le corpus  et il faut d'abord telecharger Spacy avec "pip install spacy"'

@author: lydia
"""

import spacy
import pandas as pd
from datasets import Dataset, DatasetDict
import nltk

# Télécharger les données nécessaires pour nltk
nltk.download('punkt')

# Charger le modèle de langue anglais de SpaCy
nlp = spacy.load("en_core_web_sm")

# Fonction pour tokenizer et annoter un texte
def tokenize_and_annotate_text(text):
    # Tokenization avec nltk
    tokens = nltk.word_tokenize(text)
    tokenized_text = ' '.join(tokens)
    
    # Annotation avec SpaCy
    doc = nlp(tokenized_text)
    annotations = [(token.text, token.pos_, token.tag_, token.dep_, token.head.text) for token in doc]
    
    return annotations

# Charger le Dataset Hugging Face
dataset = Dataset.from_csv('//home/lydia/Documents/outil/Bonoutput2Validated.csv')

# Annoter les données
annotations = []

for i, row in enumerate(dataset):
    context = row['context']
    annotated_context = tokenize_and_annotate_text(context)
    annotations.append({
        'table': row['table'],
        'context': row['context'],
        'annotations': annotated_context
    })

# Convertir les annotations en DataFrame
annotations_df = pd.DataFrame(annotations)

# Sauvegarder les annotations dans un nouveau fichier CSV
output_file = '/home/lydia/Documents/outil/Bonoutput2Annotated.csv'
annotations_df.to_csv(output_file, index=False)

print(f"Annotations saved to {output_file}")
