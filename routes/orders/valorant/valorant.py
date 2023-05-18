# routes1.py
from fastapi import APIRouter,HTTPException, Depends, Request
from pydantic import BaseModel
from config import * 
import jwt
from validations.lol_validation import RankBoost, DuoBoost, WinBoost, PlacementsBoost, NormalBoost
from database.db_valorant_crud import VALORANT_CRUD
from fastapi.security import OAuth2PasswordBearer
from valorantPricing import rankBoostPrice  

app = APIRouter(
    prefix="/valorant",
    tags=["valorant-orders"]
)

requireToken = OAuth2PasswordBearer(tokenUrl="auth/login")

def validate_token(token):
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except:
        raise HTTPException(status_code=400, detail="Invalid token format!")
    return decoded

@app.post("/rank-boost")
async def rank_boost(order: RankBoost, token: str = Depends(requireToken)):
    decoded = validate_token(token)
    order.user_id = decoded["user_id"]
    order.order_type = "rank_boost"

    valorant_crud = VALORANT_CRUD()
    try:
        valorant_crud.create_rank_boost(order)
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

@app.post("/win-boost")
async def win_boost(order: WinBoost, token: str = Depends(requireToken)):
    decoded = validate_token(token)
    order.user_id = decoded["user_id"]
    order.order_type = "win_boost"
    
    valorant_crud = VALORANT_CRUD()
    try:
        valorant_crud.create_win_boost(order)
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
async def placement_boost(order: PlacementsBoost, token: str = Depends(requireToken)):
    decoded = validate_token(token)
    order.user_id = decoded["user_id"]
    order.order_type = "placement_boost"
    

    valorant_crud = VALORANT_CRUD()
    try:
        valorant_crud.create_placement_boost(order)
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

@app.post("/unrated-boost")
async def unrated_boost(order: NormalBoost, token: str = Depends(requireToken)):
    decoded = validate_token(token)
    order.user_id = decoded["user_id"]
    order.order_type = "unrated_boost"
    
    valorant_crud = VALORANT_CRUD()
    try:
        order.user_id = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])['user_id']
    except Exception as e:
        print(f"HATA : {e}")
        raise HTTPException(status_code=400, detail="Invalid token format!")
    
    valorant_crud = VALORANT_CRUD()
    try:
        valorant_crud.create_normal_boost(order)
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


