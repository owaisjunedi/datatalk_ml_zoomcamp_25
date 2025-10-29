# 1. Prediction Code by importing the Model (from Binary File) and using it

import pickle
import uvicorn

from typing import Literal
from pydantic import BaseModel, Field
from fastapi import FastAPI

# class CustomerData(BaseModel):
#     lead_source: Literal["organic_search", "paid_ads", "referral", "social_media"]
#     number_of_courses_viewed: int = Field(..., ge=0)
#     annual_income: float = Field(..., ge=0.0)

# class PredictResponse(BaseModel):
#     subscribe_probability: float
#     subscribe: bool

app = FastAPI(title="customer-subscription-prediction")

model_file = 'pipeline_v1.bin'

with open(model_file, 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(customer):
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)


from typing import Dict, Any

@app.post("/predict")
def predict(customer: Dict[str, Any]):
    prob = predict_single(customer)

    return {
        "subscribe_probability": prob,
        "subscribe": bool(prob >= 0.5)
    }

# @app.post('/predict')
# def predict(customer: CustomerData) -> PredictResponse:
#     prob = predict_single(customer.model_dump())

#     return PredictResponse(
#         subscribe_probability=prob,
#         subscribe=prob >= 0.5
#     )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
