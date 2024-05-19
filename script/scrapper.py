#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
c'est le script qui permet de scrapper du site https://en.wikipedia.org/wiki/Special:RandomInCategory/Living_people
pour construire le corpus brut'
@author: lydia
"""

import requests
from bs4 import BeautifulSoup
import csv
import time
# la fonction qui récupère les url valide de wikipedia
def get_biography_urls(num_urls):
    base_url = "https://en.wikipedia.org/wiki/Special:RandomInCategory/Living_people"
    biography_urls = []
    for _ in range(num_urls):
        try:
            response = requests.get(base_url, timeout=10)
            response.raise_for_status()  # Vérifie les erreurs HTTP
            soup = BeautifulSoup(response.text, 'html.parser')
            biography_url = soup.find('link', {'rel': 'canonical'})['href']
            biography_urls.append(biography_url)
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la récupération de l'URL : {e}")
            time.sleep(5)  # Attendre avant de réessayer
    return biography_urls
# scrappe les information de l'infobox ainsi que du premier paragraphe
def scrape_wikipedia_biographies(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        infobox_table = soup.find('table', {'class': 'infobox'})
        infobox_data = {}
        if infobox_table:
            headers = infobox_table.find_all('th', {'scope': 'row'})
            content = infobox_table.find_all('td', {'class': 'infobox-data'})
            for header, item in zip(headers, content):
                key = header.text.strip().lower().replace(' ', '_')
                value = item.text.strip()
                infobox_data[key] = value

        paragraphs = soup.find_all('p')
        matching_paragraphs = []
        for paragraph in paragraphs:
            for key in infobox_data.keys():
                if key in paragraph.text.lower():
                    matching_paragraphs.append(paragraph.text.strip())

        if not matching_paragraphs:
            return None

        table_data = {
            "column_header": list(infobox_data.keys()),
            "row_number": [1] * len(infobox_data),
            "content": list(infobox_data.values())
        }

        return {
            "table": table_data,
            "context": '\n'.join(matching_paragraphs)
        }
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'extraction de la biographie : {e}")
        return None
##### limiter le nombre de page à1000 pour ne pas avoir de'erreur reseau
num_urls = 1000
biography_urls = get_biography_urls(num_urls)
##### remplir le fichier csv qui contiendra les données scrappées
with open('raw.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['table', 'context']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i, url in enumerate(biography_urls, start=1):
        page_data = scrape_wikipedia_biographies(url)
        if page_data:
            writer.writerow(page_data)
            print(f"Biographie {i}/{num_urls} extraite avec succès.")
        else:
            print(f"Impossible d'extraire la biographie {i}/{num_urls}.")
