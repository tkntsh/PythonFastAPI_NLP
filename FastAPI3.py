from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

#define input model
class FileInput(BaseModel):
    file_path: str

@app.post("/keywords")
async def extractKeywords(input: FileInput):
    try:
        #read CSV file
        df = pd.read_csv(input.file_path)
        if 'feedback' not in df.columns:
            raise HTTPException(status_code=400, detail="CSV must contain a 'feedback' column")
        
        #extract text data
        texts = df['feedback'].dropna().tolist()
        if not texts:
            raise HTTPException(status_code=400, detail="No valid feedback data found")
        
        #apply TF-IDF
        vectorizer = TfidfVectorizer(max_features=5, stop_words='english')
        tfidfMatrix = vectorizer.fit_transform(texts)
        keywords = vectorizer.get_feature_names_out()
        scores = tfidfMatrix.toarray().mean(axis=0)
        
        # Return top 5 keywords with scores
        result = [{"keyword": kw, "score": round(score, 4)} for kw, score in zip(keywords, scores)]
        return {"keywords": result}
    except Exception as e:
        raise HTTPException(statusCode=500, detail=f"Error processing CSV: {str(e)}")

# Example usage: Run with `uvicorn filename:app --reload`
# Example CSV (feedback.csv):
# feedback
# "Great product but slow delivery"
# "Amazing service, very reliable"