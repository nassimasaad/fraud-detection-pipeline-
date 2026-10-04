from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load(
    "random_forest_fraud_model.pkl"
)

@app.get("/")
def home():

    return {
        "message": "Fraud Detection API"
    }

def predict_fraud(transaction):

    df = pd.DataFrame([transaction])

    pred = model.predict(df)[0]

    prob = model.predict_proba(df)[0][1]

    return {
        "prediction": int(pred),
        "fraud_probability": float(prob)
    }

from pydantic import BaseModel
class Transaction(BaseModel):

    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float
    balance_diff_orig: float
    balance_diff_dest: float
    orig_rel_amount: float
    dest_rel_amount: float   
@app.post("/predict")
def predict(transaction: Transaction):

    result = predict_fraud(
        transaction.dict()
    )

    return result 

@app.get("/health")
def health():
    return {
        "status": "ok",
        "model": "Random Forest",
        "version": "1.0"
    }        