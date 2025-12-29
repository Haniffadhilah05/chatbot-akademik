import json
import random
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Download komponen NLTK
nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load data intents
with open('data/intents.json') as file:
    intents = json.load(file)

corpus = []
labels = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        corpus.append(pattern)
        labels.append(intent['tag'])

# Preprocessing teks
corpus = [lemmatizer.lemmatize(word.lower()) for word in corpus]

# Konversi teks ke vektor
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# Encode label
unique_labels = list(set(labels))
y = np.array([unique_labels.index(label) for label in labels])

# Latih model
model = MultinomialNB()
model.fit(X, y)

# Simpan model dan vectorizer
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
with open('labels.pkl', 'wb') as f:
    pickle.dump(unique_labels, f)

print("✅ Model chatbot berhasil dilatih dan disimpan!")
