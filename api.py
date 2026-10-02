import joblib
import pandas as pd

model = joblib.load("random_forest_fraud_model.pkl")


def predict_fraud(transaction):
    
    df = pd.DataFrame([transaction])

    pred = model.predict(df)[0]

    prob = model.predict_proba(df)[0][1]

    return {
        "prediction": int(pred),
        "fraud_probability": float(prob)
    }