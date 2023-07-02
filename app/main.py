from fastapi import FastAPI
import pickle
import numpy as np


logreg = pickle.load(open("app/logreg.pickle", "rb"))
app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Get Score!"}

@app.get("/get_score")
async def get_score(x: float, y: float):
    data = np.array([x, y])[None]
    score = logreg.predict_proba(data)[0, 0]
    return {"score": score}