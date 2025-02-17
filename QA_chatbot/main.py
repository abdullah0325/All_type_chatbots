from fastapi import FastAPI
from utils import get_response

app = FastAPI()

@app.get("/")
def chat(prompt):
    try:
        return get_response(prompt)
    except Exception as e:
        return {"error": str(e)}

