import json
import random
import pickle
import numpy as np
from nltk.stem import WordNetLemmatizer

# Load model
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
labels = pickle.load(open('labels.pkl', 'rb'))

# Load intents
with open('data/intents.json') as file:
    intents = json.load(file)

lemmatizer = WordNetLemmatizer()

def get_response(message):
    # Preprocess input
    message = message.lower()
    vect = vectorizer.transform([message])

    # Predict label
    prediction = model.predict(vect)[0]
    tag = labels[prediction]

    # Cari responses berdasarkan tag
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

    return "Maaf, aku belum mengerti maksud kamu."
