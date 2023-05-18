from pydantic import BaseModel

class RankBoostPrice(BaseModel):
    server : str
    current_rank : list
    current_lp : int
    desired_rank : list
    priority_boost : bool | None
    stream_games: bool | None
    solo_only: bool | None

class WinBoostPrice(BaseModel):
    server : str
    current_rank : list  
    wins_amount : int
    play_with_booster: bool | None
    priority_boost: bool | None
    stream_games: bool | None
    solo_only: bool | None

class PlacementsBoostPrice(BaseModel):
    server : str
    previous_rank : list  
    wins_amount : int
    play_with_booster: bool | None
    priority_boost: bool | None
    stream_games: bool | None
    solo_only: bool | None

class UnratedBoostPrice(BaseModel):
    server : str
    wins_amount : int
    game_mode: str
    play_with_booster: bool | None
    priority_boost: bool | None
    stream_games: bool | None
    solo_only: bool | None