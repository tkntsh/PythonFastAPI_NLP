#Core NLP concepts: accepts a text input and performs Named Entity Recognition (NER) to identify entities
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spacy

app = FastAPI()

#load spaCy model
nlp = spacy.load("en_core_web_sm")

#define input model
class TextInput(BaseModel):
    text: str

@app.post("/ner")
async def extractEntities(input: TextInput):
    try:
        #process text with spaCy
        doc = nlp(input.text)
        #extract entities
        entities = [{"text": ent.text, "type": ent.label_} for ent in doc.ents]
        return {"entities": entities}
    except Exception as e:
        raise HTTPException(statusCode=500, detail=f"Error processing text: {str(e)}")
    
#how to run:

# 1.Run: uvicorn ner:app --reload

# 2. Send a POST request to http://localhost:8000/ner with JSON

# {"text": "Apple is launching a new product in Cape Town."}