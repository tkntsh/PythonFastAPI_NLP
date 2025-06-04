#string manipulation API: data structures, operations
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import string

app = FastAPI()

#define input model
class TextListInput(BaseModel):
    texts: List[str]

@app.post("/word_frequency")
async def countWordFrequency(input: TextListInput):
    try:
        #initialize dictionary for word counts
        wordCounts = {}
        
        #process each text
        for text in input.texts:
            #remove punctuation and convert to lowercase
            text = text.translate(str.maketrans("", "", string.punctuation)).lower()
            #split into words and filter
            words = [word for word in text.split() if len(word) >= 3]
            #count frequencies
            for word in words:
                wordCounts[word] = wordCounts.get(word, 0) + 1
        
        return {"word_frequencies": wordCounts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")
    
#how to run:

# 1. Run: uvicorn word_frequency:app --reload (cmd)

# 2. Send a POST request to http://localhost:8000/wordFrequency with JSON below:

# {
#  "texts": ["Great product!", "Product is good but slow delivery"]
# }