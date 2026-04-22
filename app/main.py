from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import graph
from app.memory import get_history

app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    result = graph.invoke({
        "user_id": req.user_id,
        "question": req.message,
        "history": get_history(req.user_id),
        "route": ""
    })

    return result


@app.get("/")
def root():
    return {"status": "ok", "message": "LangGraph API running"}