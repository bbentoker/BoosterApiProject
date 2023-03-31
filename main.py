from fastapi import FastAPI
from routes.orders.lol.lol import app as lol
from auth.auth import app as auth
from routes.users.user import app as user
from routes.users.booster import app as booster
from routes.users.moderator import app as moderator
app = FastAPI()

app.include_router(auth)
app.include_router(user)
app.include_router(booster)
app.include_router(moderator)
app.include_router(lol)





