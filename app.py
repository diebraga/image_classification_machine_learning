from fastai.vision.all import *
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
learn = load_learner('dog_or_park.pkl')

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    is_dog,_,probs = learn.predict(await file.read())

    if str(is_dog) == 'dog':
        return {
            'prediction': 'is dog',
            'probability': str(probs[1])
        }
    else:
        return {
            'prediction': 'not a dog',
            'probability': str(probs[1])
        }

