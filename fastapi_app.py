from fastapi import FastAPI
from pydantic import BaseModel
from pyabsa import AspectPolarityClassification as APC

app = FastAPI()

class Item(BaseModel):
    userText: str
    modelType: str

def getSentiments(userText, type):
    sentiment_classifier = APC.SentimentClassifier("\Model-PyABSA\checkpoints")
    if type == 'SentimentClassifier - Prabowo':
        target_word = "prabowo"
    elif type == 'SentimentClassifier - Ganjar':
        target_word = "ganjar"
    elif type == 'SentimentClassifier - Anies':
        target_word = "anies"
    replacement_start = "[B-ASP]"
    replacement_end = "[E-ASP]"

    result_text = []

    for sent in [userText]:
        if target_word in sent.lower():
            modified_t = sent.replace(target_word, f"{replacement_start}{target_word}{replacement_end}")
            result_text.append(modified_t)
        else:
            result_text.append(userText)

    text = sentiment_classifier.predict(
        text=result_text,
        save_result=True,
        print_result=True,
        ignore_error=True,
    )
    sentiment = text[0]["sentiment"][0]
    confidence = text[0]["confidence"][0]

    return sentiment, confidence

@app.post("/predict")
async def predict(item: Item):
    result, confidence = getSentiments(item.userText, item.modelType)
    return {"sentiment": result, "confidence": confidence}