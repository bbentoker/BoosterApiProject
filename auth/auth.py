import time
import jwt
import bcrypt
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends, status
from validations.user_validation import UserLogin
from database.db_users_crud import Users_CRUD
from config import *

app = APIRouter(
    prefix="/auth",
    tags=["auth"]
)




@app.post("/login")
async def login_for_access_token(form_data: UserLogin):

    user_crud = Users_CRUD()
    user = user_crud.get_user({"username": form_data.username, "password": form_data.password})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = jwt.encode({"user_id": user["id"], "role": user["role"], "expire_time": int(time.time() + 86400)}, JWT_SECRET, algorithm=JWT_ALGORITHM)
    print(f"auth token: {token}")
    return {"token": token} 


