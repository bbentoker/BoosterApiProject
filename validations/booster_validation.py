from pydantic import BaseModel


class Booster(BaseModel):
    username: str
    password: str
    email: str
    role: str | None
    about: str | None 




