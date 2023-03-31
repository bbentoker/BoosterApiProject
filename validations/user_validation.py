from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    role: str | None 


class UserEdit(BaseModel):
    user_id: int 
    username: str | None
    password: str | None
    email: str | None
    role: str | None 


class UserLogin(BaseModel):
    username: str
    password: str


