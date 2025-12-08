from xgboost import XGBClassifier as xgb
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import time as t
import joblib as jl


def train():
    # Load dataset & Drop Nonsense
    df = pd.read_csv("Train/trainingData.csv")
    df.dropna()




    X = df.iloc[:, 0:520]
    y = df["FLOOR"]

    # Train a XGBoost classifier (Tried with 2000 estimators after 1100, performed the same; 1100 is an 89.20% accuracy)
    model = xgb(n_estimators=500, max_depth=6)
    model.fit(X, y)



    jl.dump(model, "Trained_Models/XGB.joblib")
    
def test():
    df = pd.read_csv("Test/validationData.csv")
    df.dropna()
    
    X = df.iloc[:, 0:520]
    y = df["FLOOR"]
    
    model = jl.load("Trained_Models/XGB.joblib")
    
    test = model.predict(X)
    probability = model.predict_proba(X)
    accuracy = np.max(probability, axis=1)
    overall_accuracy = accuracy_score(y, test)
    
    
    try:
        for i, (pred, actual, conf) in enumerate(zip(test, y, accuracy), start=1):
            print(f"Prediction {i}: {pred}\n"
                f"Actual: {actual}\n"
                f"Confidence: {conf:.2%}\n")
            t.sleep(1)
    except:
        None
    finally:
        print(f"\nOverall Accuracy: {overall_accuracy:.2%}")
    
    
def menu():
    choice = int(input(
          "\n1. Train\n"
          "2. Test\n"
          "3. Quit\n"
          "\n-> "))
    
    match choice:
        case 1:
            train()
        case 2:
            test()
        case 3:
            exit()
        case _:
            print("Error. Quitting program")
            exit()
            
def main():
    menu()
    
if __name__ == "__main__":
    main()