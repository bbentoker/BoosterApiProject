from fastapi import APIRouter, HTTPException
from validations.booster_validation import Booster
from database.db_boosters_crud import Boosters_CRUD

app = APIRouter(
    prefix="/moderators",
    tags=["moderators"]
)


@app.post("/signup")
async def signup(user: Booster):
    user_crud = Boosters_CRUD()
    try:
        user.role = "user"
        user_crud.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
   
    return {"message": "Booster created"}