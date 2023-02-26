from fastai.vision.all import *
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO

app = FastAPI()
learn = load_learner('dog_or_park.pkl')

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(BytesIO(contents))
    pred, _, probs = learn.predict(img)
    return {
        'prediction': str(pred),
        'probability': str(probs[1])
    }
