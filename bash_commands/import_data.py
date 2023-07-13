from elasticsearch import Elasticsearch
from faker import Faker
from hugging_request import query
from random import randint
import csv


def hugging_predict(text):
    output = query({
        "inputs": text,
    })
    if type(output) == list:
        return output[0][0]["label"].capitalize()
    
    return []


# Connexion à Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200,'scheme': 'http'}])

# Nom de l'index Elasticsearch
index_name = 'textes'

def delete_all(es,index_name):
        # Define the query to match all documents
    query = {
        "query": {
            "match_all": {}
        }
    }

    # Delete documents using the delete_by_query API
    response = es.delete_by_query(index=index_name, body=query)

delete_all(es,index_name)


# Instanciation de Faker
fake = Faker()

# Fake patient


# Chemin vers le fichier CSV
csv_file = '../src/emotion_final.csv'


# Lecture du fichier CSV et indexation des données
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Génération des valeurs Faker pour les champs nom et prenom
        row['patient_id'] = randint(3,60)
        row['emotion'] = hugging_predict([row['text']])
        row['date'] =  fake.date_between(start_date='-30d', end_date='today').strftime("%Y-%m-%d")
        # Indexation des données dans Elasticsearch
        es.index(index=index_name, document=row)
es.indices.refresh(index=index_name)
es.transport.close()
print("Indexation terminée.")