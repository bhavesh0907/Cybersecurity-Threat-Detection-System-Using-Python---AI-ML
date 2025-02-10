from feature_extraction import extract_features
from model import load_model, predict

def main():
    print("Cybersecurity Threat Detection System Initialized...")
    file_path = input("Enter the file path to scan: ")
    features = extract_features(file_path)
    model = load_model()
    prediction = predict(model, features)
    print("Threat Level:", prediction)

if __name__ == "__main__":
    main()
