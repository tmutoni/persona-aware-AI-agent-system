from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="Persona Classifier (stub)")

class Event(BaseModel):
    user_id: str
    path: str
    ts: float

PERSONAS = ["photo_first", "vector_first", "general_creator"]

@app.post("/classify")
def classify(event: Event):
    return {"user_id": event.user_id, "persona": random.choice(PERSONAS)}
