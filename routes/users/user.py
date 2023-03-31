from fastapi import APIRouter, HTTPException
from validations.user_validation import UserCreate, UserEdit
from database.db_users_crud import Users_CRUD

app = APIRouter(
    prefix="/users",
    tags=["users"]
)


@app.post("/signup")
async def signup(user: UserCreate):
    user_crud = Users_CRUD()
    try:
        user.role = "user"
        user_crud.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
   
    return {"message": "User created"}

@app.post("/edit")
async def signup(user: UserEdit):
    user_crud = Users_CRUD()
    try:
        user.role = "user"
        user_crud.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
   
    return {"message": "User created"}