
from fastapi import FastAPI, UploadFile, File

from utils import generate_response, create_store_embedding

app = FastAPI()
@app.post ("/store_embedding")
def store_embedding( index_name: str ,file: UploadFile=File(...)):
    try:
        result = create_store_embedding(file, index_name)
        return result
    except Exception as e:
        return {"error": str(e)}

@app.post("/generate_response")
def get_response(question, index_name: str):
    try:
        response = generate_response(question, index_name)
        return response
    except Exception as e: 
        return {"error": str(e)}
    
