from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from plato_mini import dialog_predict

class MessageInput(BaseModel):
    history: List[str]

class MessageOutput(BaseModel):
    response: str


app = FastAPI()

@app.get('/')
async def index() -> str:
    return 'OK'

@app.post('/messages')
async def respond_messages(input: MessageInput) -> MessageOutput:
    return MessageOutput(response=dialog_predict(input.history))
