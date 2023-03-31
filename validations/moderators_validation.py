from pydantic import BaseModel


class Moderator(BaseModel):
    username: str
    password: str
    email: str
    role: str | None 



