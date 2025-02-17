from fastapi import FastAPI, Query
from util import get_response

app = FastAPI()


@app.get("/chat/")
def chat_bot(user_query: str):
    try:
        response = get_response(user_query)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
    