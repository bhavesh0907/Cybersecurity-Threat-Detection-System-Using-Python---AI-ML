from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle

def train():
    X_train = np.array([[500], [1000], [1500], [2000], [5000]])
    y_train = np.array([0, 0, 1, 1, 1])
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X_train, y_train)
    with open("cybersecurity_model.pkl", "wb") as file:
        pickle.dump(model, file)
    print("Model trained and saved.")

if __name__ == "__main__":
    train()
