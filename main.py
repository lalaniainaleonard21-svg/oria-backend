from fastapi import FastAPI
import os
from groq import Groq

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Oria Backend Python OK"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/test-env")
def test_env():
    key = os.environ.get("GROQ_API_KEY")
    return {"groq_key_loaded": bool(key)}
