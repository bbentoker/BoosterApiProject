from pydantic import BaseModel

class RankBoost(BaseModel):
    user_id: int | None
    order_type : str | None
    current_rank : str
    current_lp: str
    server: str
    desired_rank: str
    q_type: str
    champions_roles: bool 
    priority_boost: bool
    stream_games: bool
    solo_only: bool
    bonus_win: bool
    total_price: float

class RankBoostPrice(BaseModel):
    server : str
    current_rank : list
    current_lp : int
    desired_rank : list
    priority_boost: bool | None
    stream_games: bool | None
    solo_only: bool | None

class DuoBoost(BaseModel):
    user_id: int | None
    order_type : str | None
    current_rank : str
    current_lp: str
    server: str
    desired_rank: str
    q_type: str
    champions_roles: bool
    priority_boost: bool
    bonus_win: bool
    total_price: float

class DuoBoostPrice(BaseModel):
    server : str
    current_rank : list
    current_lp : int
    desired_rank : list
    priority_boost: bool | None
    stream_games: bool | None
    solo_only: bool | None


class WinBoost(BaseModel):
    user_id: int | None
    order_type : str | None
    current_rank : str
    server: str
    wins_amount: int
    q_type: str
    play_with_booster: bool
    champions_roles: bool
    priority_boost: bool
    stream_games: bool
    solo_only: bool
    total_price: float
    
class WinBoostPrice(BaseModel):
    server : str
    current_rank : list  
    wins_amount : int
    play_with_booster: bool | None
    priority_boost: bool | None
    stream_games: bool | None
    solo_only: bool | None

class PlacementsBoost(BaseModel):
    user_id: int | None
    order_type : str | None
    previous_rank: str
    server: str
    q_type: str
    wins_amount: int
    play_with_booster: bool
    champions_roles: bool
    priority_boost: bool
    stream_games: bool
    solo_only: bool
    total_price: float

class PlacementsBoostPrice(BaseModel):
    server : str
    previous_rank : list  
    wins_amount : int
    play_with_booster: bool | None
    priority_boost: bool | None
    stream_games: bool | None
    solo_only: bool | None


class NormalBoost(BaseModel):
    user_id: int | None
    order_type : str | None
    games_amount: int
    game_mode: str
    server: str
    play_with_booster: bool
    champions_roles: bool
    priority_boost: bool
    stream_games: bool
    solo_only: bool
    total_price: float

class NormalBoostPrice(BaseModel):
    server : str
    wins_amount : int
    game_mode: str
    play_with_booster: bool | None
    priority_boost: bool | None
    stream_games: bool | None
    solo_only: bool | None