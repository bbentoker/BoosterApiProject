from pydantic import BaseModel

class MessageValidation(BaseModel):
    client_id: int
    receiver_id: int
    message: str
    read: str
