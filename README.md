# FastAPI NLP Preprocessing API

## Overview

This is a simple **FastAPI-based** web service that provides natural language preprocessing capabilities. It accepts raw text via a POST request and returns a list of **cleaned, lemmatized tokens**, having removed stopwords and punctuation.

### Features

* **Tokenization** using NLTK
* **Stopword removal** (English)
* **Lemmatization** using WordNet
* Built with **FastAPI** for fast, async-ready HTTP API

---

## Requirements

Install the required Python packages:

```bash
pip install fastapi uvicorn nltk pydantic
```

> Note: The first time you run the app, it downloads NLTK corpora (punkt, stopwords, wordnet).

---

## How to Run

1. Save the script as `FastAPI1.py`.
2. Launch the server using Uvicorn:

   ```bash
   uvicorn FastAPI1:app --reload
   ```
3. Access the interactive API docs:

   * Open your browser and go to: `http://127.0.0.1:8000/docs`

---

## API Endpoint

### `POST /preprocess`

**Description:** Accepts a JSON object with raw text and returns cleaned tokens.

**Request Body:**

```json
{
  "text": "Your input text goes here."
}
```

**Response:**

```json
{
  "tokens": ["lemmatized", "word1", "word2"]
}
```

**Example using curl:**

```bash
curl -X POST "http://127.0.0.1:8000/preprocess" \
-H "Content-Type: application/json" \
-d '{"text": "Cats are running faster than dogs!"}'
```

---

## Notes

* Make sure you have internet access when running for the first time, as it downloads NLTK corpora.
* For production use, pre-download NLTK data and manage error handling/logging appropriately.

---

## Author

**Ntshangase Ntokozo**
**Project: NLP Preprocessing with FastAPI**
