import hashlib
import os

def extract_features(file_path):
    features = {}
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            features['size'] = len(data)
            features['hash'] = hashlib.md5(data).hexdigest()
    except FileNotFoundError:
        print("File not found.")
        return None
    return features
