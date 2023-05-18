# routes1.py
from fastapi import APIRouter,HTTPException, Request, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from config import * 
import jwt
from validations.chat_validation import MessageValidation
from database.db_chat_crud import CHAT_CRUD
from fastapi.security import OAuth2PasswordBearer
import time
import json

app = APIRouter(
    prefix="/chat",
    tags=["chat-operations"]
)

requireToken = OAuth2PasswordBearer(tokenUrl="auth/login")

def validate_token(token):
    
    expired = False
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if(decoded["expire_time"] < int(time.time())):
            return False
    except:
        return False

    return True


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

@app.websocket("/ws/{client_id}/{receiver_id}/{token}")
async def websocket_endpoint(websocket: WebSocket, client_id: int,receiver_id:int, token: str):
    # if(not validate_token(token)):
    #     manager.disconnect(websocket)
    
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            chat_crud = CHAT_CRUD()
            database_data: MessageValidation = {
                "client_id":client_id,
                "receiver_id":receiver_id,
                "message":data,
                "read":False
            }
            await chat_crud.create(database_data)
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            # await manager.broadcast(f"Client #{client_id} says: {data}")
            await manager.broadcast(json.dumps({'client_id': client_id, "receiver_id" :receiver_id,  "data":data}))
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")

