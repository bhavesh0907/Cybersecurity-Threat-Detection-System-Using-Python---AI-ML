from model import load_model, predict

def test():
    test_samples = [{'size': 800}, {'size': 2500}, {'size': 6000}]
    model = load_model()
    for sample in test_samples:
        result = predict(model, sample)
        print(f"Test Sample {sample}: {result}")

if __name__ == "__main__":
    test()
