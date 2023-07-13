from dotenv import load_dotenv
import requests
import os

load_dotenv()

hugging_key = os.getenv("HUGGING_KEY")

API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
headers = {"Authorization": hugging_key}

def query(text):
	payload = {
	"text": text
}
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()