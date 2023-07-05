import csv
from faker import Faker
from elasticsearch import Elasticsearch

fake = Faker()
es = Elasticsearch(["localhost:9200"])

# Générer et indexer des documents dans l'index "notes"
for _ in range(100):
    document = {
        "patient_lastname": fake.last_name(),
        "patient_firstname": fake.first_name(),
        "text": fake.text(),
        "date": fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
        "patient_left": fake.boolean(),
        "emotion": None,  # Champ à remplir avec le modèle
        "confidence": None  # Champ à remplir avec le modèle
    }
    es.index(index="notes", body=document)