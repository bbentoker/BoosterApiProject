from fastapi import APIRouter
from validations.lol_validation import (
    RankBoostPrice,
    DuoBoostPrice,
    WinBoostPrice,
    PlacementsBoostPrice,
    NormalBoostPrice,
)
import lolPricing

app = APIRouter(prefix="/lol_pricing", tags=["lol_pricing"])


@app.post("/rank-boost-price")
async def rankBoostPrice(order: RankBoostPrice):
    return lolPricing.rankBoostPrice(
        order.server,
        order.current_rank,
        order.current_lp,
        order.desired_rank,
        order.priority_boost,
        order.stream_games,
        order.solo_only,
    )


@app.post("/duo-boost-price")
async def duoBoostPrice(order: DuoBoostPrice):
    return lolPricing.duoBoostPrice(
        order.server,
        order.current_rank,
        order.current_lp,
        order.desired_rank,
        order.priority_boost,
        order.stream_games,
        order.solo_only,
    )


@app.post("/win-boost-price")
async def duoBoostPrice(order: WinBoostPrice):
    return lolPricing.winBoostPrice(
        order.server,
        order.current_rank,
        order.wins_amount,
        order.play_with_booster,
        order.priority_boost,
        order.stream_games,
        order.solo_only,
    )


@app.post("/placements-boost-price")
async def placementBoostPrice(order: PlacementsBoostPrice):
    return lolPricing.placementsBoostPrice(
        order.server,
        order.previous_rank,
        order.wins_amount,
        order.play_with_booster,
        order.priority_boost,
        order.stream_games,
        order.solo_only,
    )


@app.post("/normals-boost-price")
async def normalsBoostPrice(order: NormalBoostPrice):
    return lolPricing.normalsBoostPrice(
        order.server,
        order.game_mode,
        order.wins_amount,
        order.play_with_booster,
        order.priority_boost,
        order.stream_games,
        order.solo_only,
    )
