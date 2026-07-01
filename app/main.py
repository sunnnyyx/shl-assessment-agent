from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.agent import chat

app = FastAPI(
    title="SHL Assessment Recommender",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "SHL Assessment Recommender API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.post("/chat")
def chat_endpoint(request: ChatRequest):

    response = chat(
        [m.model_dump() for m in request.messages]
    )

    return response