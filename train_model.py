import json
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load intents
with open('data/intents.json', 'r') as file:
    data = json.load(file)

# Siapkan data training
patterns = []
tags = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern.lower())
        tags.append(intent['tag'])

# Vectorizer (mengubah teks jadi angka)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)

# Encode label/tag jadi angka
unique_tags = list(set(tags))
label_map = {tag: i for i, tag in enumerate(unique_tags)}
y = np.array([label_map[tag] for tag in tags])

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
pickle.dump(unique_tags, open('labels.pkl', 'wb'))

print("Training selesai! Model berhasil dibuat.")

