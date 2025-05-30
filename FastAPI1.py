from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

app = FastAPI()

# Define input model
class TextInput(BaseModel):
    text: str

# Initialize NLTK tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

@app.post("/preprocess")
async def preprocess_text(input: TextInput):
    try:
        # Tokenize
        tokens = word_tokenize(input.text.lower())
        # Remove stop words and non-alphabetic tokens
        tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
        # Lemmatize
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return {"tokens": tokens}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")

# Example usage: Run with `uvicorn filename:app --reload`