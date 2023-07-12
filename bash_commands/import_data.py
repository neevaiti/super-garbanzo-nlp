from elasticsearch import Elasticsearch
from faker import Faker
import csv
import random
import pickle
from preprocessing import TextPreprocessor




# Load the pickle file
pickle_path = "/Users/maximer/Documents/Dev/Python/Projets/elasticsearch-nlp-sentiment_analysis/analyse/nlp_pipeline.pkl"
with open(pickle_path, 'rb') as file:
    model = pickle.load(file)

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
csv_file = 'elasticsearch-nlp-sentiment_analysis/Emotion_final.csv'

from random import randint

# Lecture du fichier CSV et indexation des données
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Génération des valeurs Faker pour les champs nom et prenom
        row['patient_id'] = randint(3,60)
        row['emotion'] = model.predict([row['text']])[0]
        row['confidence'] = model.predict_proba([row['text']]).max()
        row['date'] =  fake.date_between(start_date='-30d', end_date='today').strftime("%Y-%m-%d")
        # Indexation des données dans Elasticsearch
        es.index(index=index_name, document=row)
es.indices.refresh(index=index_name)
es.transport.close()
print("Indexation terminée.")