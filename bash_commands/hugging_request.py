from dotenv import load_dotenv
import logging
import requests
import os

load_dotenv()

hugging_key = os.getenv("HUGGING_KEY")

API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
headers = {"Authorization": hugging_key}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def init():
	query({"inputs": "test"})
	logging.log(level= 1, msg= "Hugging face model initialisated")
	