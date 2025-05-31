from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Define input model
class TextInput(BaseModel):
    text: str

# Initialize Hugging Face sentiment analysis pipeline
sentimentAnalyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.post("/sentiment")
async def analyzeSentiment(input: TextInput):
    try:
        # Perform sentiment analysis
        result = sentimentAnalyzer(input.text)[0]
        sentiment = result['label'].lower()
        confidence = result['score']
        return {"sentiment": sentiment, "confidence": round(confidence, 4)}
    except Exception as e:
        raise HTTPException(statusCode=500, detail=f"Error analyzing sentiment: {str(e)}")

# Example usage: Run with `uvicorn filename:app --reload`