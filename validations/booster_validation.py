from pydantic import BaseModel


class Booster(BaseModel):
    username: str
    password: str
    email: str
    user_role: str | None
    about: str | None 
    boost_type: str | None
    server: str | None
    rank: str | None
    game_role: str | None
    details: str | None
    price: int | None

