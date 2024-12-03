from fastapi import FastAPI, requests
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Change this in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("scores.csv")


@app.get("/get-Score/{pointsW}/{pointsL}")
def get_scores(pointsW: str, pointsL: str):
    score = f"{pointsW}-{pointsL}"

    if score in df["Score"].values:
        return {"message": "not Scoragami", "score": score}
    
    return {"message": "Scoragami", "score": score}