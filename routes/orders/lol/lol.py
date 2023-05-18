# routes1.py
from fastapi import APIRouter,HTTPException, Depends, Request
from config import * 
import jwt
from validations.lol_validation import RankBoost, DuoBoost, WinBoost, PlacementsBoost, NormalBoost
from database.db_lol_crud import LOL_CRUD
from fastapi.security import OAuth2PasswordBearer
import time

app = APIRouter(
    prefix="/lol",
    tags=["lol-orders"]
)

requireToken = OAuth2PasswordBearer(tokenUrl="auth/login")

def validate_token(token):
    token = token.replace("Bearer ", "")
    print("AUTHORIZATION HEADER: ", token)
    expired = False
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if(decoded["expire_time"] < int(time.time())):
            expired = True
    except:
        raise HTTPException(status_code=400, detail="Invalid token format!")
    
    if(expired):
        raise HTTPException(status_code=400, detail="Token expired!")
    return decoded



@app.post("/rank-boost")
async def rank_boost(order: RankBoost, request: Request):
    decoded = validate_token(request.headers.get("Authorization"))
    order.user_id = decoded["user_id"]
    order.order_type = "rank_boost"
    
    lol_crud = LOL_CRUD()
    try:
        lol_crud.create_rank_boost(order)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"message": {
        "current_rank": order.current_rank,
        "current_lp": order.current_lp,
        "server": order.server,
        "desired_rank": order.desired_rank,
        "q_type": order.q_type,
        "champions_roles": order.champions_roles,
        "priority_boost": order.priority_boost,
        "stream_games": order.stream_games,
        "solo_only": order.solo_only,
        "bonus_win": order.bonus_win,
        "total_price": order.total_price
    }
}


@app.post("/duo-boost")
async def duo_boost(order: DuoBoost,request: Request):
    decoded = validate_token(request.headers.get("Authorization"))
    order.user_id = decoded["user_id"]
    order.order_type = "duo_boost"

    lol_crud = LOL_CRUD()
    try:
        lol_crud.create_duo_boost(order)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"message": {    
        "current_rank": order.current_rank,
        "current_lp": order.current_lp,
        "server": order.server,
        "desired_rank": order.desired_rank,
        "q_type": order.q_type,
        "champions_roles": order.champions_roles,
        "priority_boost": order.priority_boost,
        "bonus_win": order.bonus_win,
        "total_price": order.total_price
    }}

@app.post("/win-boost")
async def win_boost(order: WinBoost,request: Request):
    decoded = validate_token(request.headers.get("Authorization"))
    order.user_id = decoded["user_id"]
    order.order_type = "win_boost"

    lol_crud = LOL_CRUD()
    try:
        lol_crud.create_win_boost(order)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": {
        "current_rank": order.current_rank,
        "server": order.server,
        "wins_amount": order.wins_amount,
        "q_type": order.q_type,
        "play_with_booster": order.play_with_booster,
        "champions_roles": order.champions_roles,
        "priority_boost": order.priority_boost,
        "stream_games": order.stream_games,
        "solo_only": order.solo_only,
        "total_price": order.total_price
    }}


@app.post("/placement-boost")
async def placement_boost(order: PlacementsBoost, request: Request):
    decoded = validate_token(request.headers.get("Authorization"))
    order.user_id = decoded["user_id"]
    order.order_type = "placement_boost"
    

    lol_crud = LOL_CRUD()
    try:
        lol_crud.create_placement_boost(order)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": {
        "previous_rank": order.previous_rank,
        "server": order.server,
        "q_type": order.q_type,
        "wins_amount": order.wins_amount,
        "play_with_booster": order.play_with_booster,
        "champions_roles": order.champions_roles,
        "priority_boost": order.priority_boost,
        "stream_games": order.stream_games,
        "solo_only": order.solo_only,
        "total_price": order.total_price
    }}

@app.post("/normal-boost")
async def normal_boost(order: NormalBoost, request: Request):

    decoded = validate_token(request.headers.get("Authorization"))
    order.user_id = decoded["user_id"]
    order.order_type = "normal_boost"
    
    lol_crud = LOL_CRUD()
    try:
        lol_crud.create_normal_boost(order)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": {
        "games_amount": order.games_amount,
        "game_mode": order.game_mode,
        "server": order.server,
        "play_with_booster": order.play_with_booster,
        "champions_roles": order.champions_roles,
        "priority_boost": order.priority_boost,
        "stream_games": order.stream_games,
        "total_price": order.total_price
    }}


