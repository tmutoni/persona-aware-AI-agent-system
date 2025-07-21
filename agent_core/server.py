from fastapi import FastAPI
from pydantic import BaseModel
import random, uvicorn

app = FastAPI(title="Persona Classifier (stub)")

class Event(BaseModel):
    user_id: str
    path: str
    ts: float

PERSONAS = ["photo_first", "vector_first", "general_creator"]

@app.post("/classify")
def classify(event: Event):
    return {"user_id": event.user_id, "persona": random.choice(PERSONAS)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
