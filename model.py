import pickle
import numpy as np

def load_model():
    with open("cybersecurity_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

def predict(model, features):
    if features is None:
        return "Invalid input"
    feature_vector = np.array([features['size']])
    result = model.predict([feature_vector])
    return "Malicious" if result[0] == 1 else "Safe"
