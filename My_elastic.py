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

# Exemple pour générer une nouvelle donnée factice
new_text = fake.text()

# Appliquez le modèle TF-IDF sur la nouvelle donnée
new_text_vectorized = vectorizer.transform([new_text])

# Prédisez l'émotion et la confiance pour la nouvelle donnée
emotion_prediction = emotion_model.predict(new_text_vectorized)
confidence_prediction = confidence_model.predict(new_text_vectorized)

# Affichez les résultats
print("Emotion prediction:", emotion_prediction)
print("Confidence prediction:", confidence_prediction)
