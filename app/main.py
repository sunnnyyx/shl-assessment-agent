from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.agent import chat

app = FastAPI(
    title="SHL Assessment Recommender",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/")
def root():
    return {
        "message": "SHL Assessment Recommender API"
    }


class Message(BaseModel):
    role: str
    content: str


class Recommendation(BaseModel):
    name: str
    url: str


class ChatResponse(BaseModel):
    reply: str
    recommendations: List[Recommendation]
    end_of_conversation: bool


class ChatRequest(BaseModel):
    messages: List[Message]


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):

    response = chat(
        [m.model_dump() for m in request.messages]
    )

    return response