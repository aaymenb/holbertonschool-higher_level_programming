Python - Serialization
This project explores data serialization in Python, covering:

Serialization with pickle – saving and loading Python objects.
JSON format (json module) – converting Python objects to JSON and vice versa.
Other formats – an overview of csv, yaml, and marshal.
📌 Quick examples:

Using pickle (binary serialization)
python
Copier
Modifier
import pickle

data = {"name": "Alice", "age": 25}

# Serialize and save to file
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

# Load from file
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
    print(loaded_data)
Using json (text-based serialization)
python
Copier
Modifier
import json

data = {"name": "Bob", "age": 30}

# Convert to JSON and save
with open("data.json", "w") as file:
    json.dump(data, file)

# Load JSON file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
