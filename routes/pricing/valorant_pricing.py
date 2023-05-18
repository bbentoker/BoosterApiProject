from fastapi import APIRouter
from validations.valorant_validations import (
    RankBoostPrice,
    WinBoostPrice,
    PlacementsBoostPrice,
    UnratedBoostPrice,
)
import valorantPricing

app = APIRouter(prefix="/valorant_pricing", tags=["valorant_pricing"])


@app.post("/rank-boost-price")
async def rankBoostPrice(order: RankBoostPrice):
    return valorantPricing.rankBoostPrice(
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
    return valorantPricing.winBoostPrice(
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
    return valorantPricing.placementsBoostPrice(
        order.server,
        order.previous_rank,
        order.wins_amount,
        order.play_with_booster,
        order.priority_boost,
        order.stream_games,
        order.solo_only,
    )


@app.post("/unrated-boost-price")
async def normalsBoostPrice(order: UnratedBoostPrice):
    return valorantPricing.unratedBoostPrice(
        order.server,
        order.game_mode,
        order.wins_amount,
        order.play_with_booster,
        order.priority_boost,
        order.stream_games,
        order.solo_only,
    )
