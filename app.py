from fastai.vision.all import *
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import gradio as gr

app = FastAPI()
learn = load_learner('model.pkl')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    prediction, _, probabilities = learn.predict(await file.read())
    probabilities = list(map(lambda p: int(round(float(p) * 100)), probabilities))
    return {
        'cat': f'{probabilities[0]}',
        'dog': f'{probabilities[1]}',
        'other': f'{probabilities[2]}',
    }
