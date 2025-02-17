from fastapi import FastAPI, UploadFile, File
from utils import create_store_embedding, generate_response

app = FastAPI()


@app.post("/upload_file")

async def upload_file(file: UploadFile = File(...)):
    try:
        embeddings = create_store_embedding(file)
        return embeddings
    except Exception as e:
        return {"error": str(e)}
    


@app.get("/chat")
def chat(usre_question: str):
    try:
        response = generate_response(usre_question)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
   