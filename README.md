# outils-de-traitement-Corpus-2023-2024
Le projet que j'ai choisi pour mon corpus est WIKI_BIO qui est disponible sur :https://huggingface.co/datasets/wiki_bio

Le WikiBio dataset est également connu sous le nom de Wikipedia Biography Dataset, comprend 728,321 biographies extraites de Wikipedia en anglais.
Chaque entrée de ce dataset contient le premier paragraphe de l'article et l'infobox associé, tous deux préalablement tokenisés.

Ce dataset est particulièrement conçu pour évaluer les algorithmes de génération de texte. Il est structuré en trois sous-ensembles : 80% pour l'entraînement, 10% pour la validation, et 10% pour le test.

Chacune des données est structurée de cette façon:
{
   "input_text":{
      "context":"pope michael iii of alexandria\n",
      "table":{
         "column_header":[
            "type",
            "ended",
            "death_date",
            "title",
            "enthroned",
            "name",
            "buried",
            "religion",
            "predecessor",
            "nationality",
            "article_title",
            "feast_day",
            "birth_place",
            "residence",
            "successor"
         ],
         "content":[
            "pope",
            "16 march 907",
            "16 march 907",
            "56th of st. mark pope of alexandria & patriarch of the see",
            "25 april 880",
            "michael iii of alexandria",
            "monastery of saint macarius the great",
            "coptic orthodox christian",
            "shenouda i",
            "egyptian",
            "pope michael iii of alexandria\n",
            "16 -rrb- march -lrb- 20 baramhat in the coptic calendar",
            "egypt",
            "saint mark 's church",
            "gabriel i"
         ],
         "row_number":[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
      }
   },
   "target_text":"pope michael iii of alexandria -lrb- also known as khail iii -rrb- was the coptic pope of alexandria and patriarch of the see of st. mark -lrb- 880 -- 907 -rrb- .\nin 882 , the governor of egypt , ahmad ibn tulun , forced khail to pay heavy contributions , forcing him to sell a church and some attached properties to the local jewish community .\nthis building was at one time believed to have later become the site of the cairo geniza .\n"
}
La tâche est : table to text
La langue: Anglais
Source: les tables ont été construite à partir des infobox contenues dans les biographie sue Wikipedia tandis que les p rties target_text, ce sont les premiers paragraphes de chacune de ces biographies.
:
## Date de publication hugging face:
2018
## Date de publication de l'article:
Neural Text Generation from Structured Data with Application to the Biography Domain 2016
## Auteurs:
Rémi Lebret, David Grangier and Michael Auli

J'ai eu la bonne idée de construire un dataset similaire et cela en élaborrants des scripts qui me permettent d'arriver au même résultat que celui de WIKI_BIO.
