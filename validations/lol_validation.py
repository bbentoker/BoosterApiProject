from pydantic import BaseModel

class RankBoost(BaseModel):
    user_id: int | None
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

class DuoBoost(BaseModel):
    user_id: int | None
    current_rank : str
    current_lp: str
    server: str
    desired_rank: str
    q_type: str
    champions_roles: bool
    priority_boost: bool
    bonus_win: bool
    total_price: float


class WinBoost(BaseModel):
    user_id: int | None
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


class PlacementBoost(BaseModel):
    user_id: int | None
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


class NormalBoost(BaseModel):
    user_id: int | None
    games_amount: int
    game_mode: str
    server: str
    play_with_booster: bool
    champions_roles: bool
    priority_boost: bool
    stream_games: bool
    solo_only: bool
    total_price: float

