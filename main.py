from fastapi import FastAPI
from routes.orders.valorant.valorant import app as valorant
from routes.orders.lol.lol import app as lol
from routes.pricing.lol_pricing import app as lolPricing
from routes.pricing.valorant_pricing import app as valorantPricing
from routes.chat.ws_chat import app as chat
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
app.include_router(lolPricing)
app.include_router(valorant)
app.include_router(valorantPricing)
app.include_router(chat)





