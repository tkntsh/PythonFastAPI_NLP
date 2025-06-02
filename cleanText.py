#NLP preprocessing: tokenization, stop-word removal, and converting tokens to lowercase
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = FastAPI()

#define input model
class TextInput(BaseModel):
    text: str

#initialize stop words
stopWords = set(stopwords.words('english'))

@app.post("/clean_text")
async def cleanText(input: TextInput):
    try:
        #tokenize and convert to lowercase
        tokens = word_tokenize(input.text.lower())
        #remove stop words and non-alphabetic tokens
        cleanedTokens = [token for token in tokens if token.isalpha() and token not in stopWords]
        return {"cleaned_tokens": cleanedTokens}
    except Exception as e:
        raise HTTPException(statusCode=500, detail=f"Error cleaning text: {str(e)}")
    
#how to run:

# 1. Run: uvicorn clean_text:app --reload

# 2. Send a POST request to http://localhost:8000/cleanText with JSON below:

# {"text": "The service is very good, but it's slow!"}