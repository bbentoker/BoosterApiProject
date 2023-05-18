import psycopg2
import jwt
import hmac
from config import *
import bcrypt
from validations.user_validation import UserCreate,UserEdit, UserLogin
from fastapi import HTTPException


class Users_CRUD:

    def get_user(self, user: UserLogin):
        conn = psycopg2.connect(
            host=DB_HOSTNAME,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )
        user_password = bytes(user['password'], 'utf-8')
        hashed_password = hmac.new(bytes(PWD_HASH_SECRET, 'utf-8'), user_password, digestmod='sha256').hexdigest()
        print(hashed_password)

        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user['username'], hashed_password))
        user = cur.fetchone()
        print(user)

        if(user == None):
            raise  HTTPException(status_code=400, detail="Invalid username or password!")
        cur.close()
        conn.close()
        print("user: ", user)
        return {
            "id": user[0],
            "username": user[1],
            "role": user[3],
            "about": user[4]
        }

    def create_user(self, user: UserCreate):
        conn = psycopg2.connect(
            host=DB_HOSTNAME,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )

        password  = bytes(user.password, 'utf-8')
        hashed_password = hmac.new(bytes(PWD_HASH_SECRET, 'utf-8'), password, digestmod='sha256').hexdigest()

        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password, role) VALUES (%s,%s,%s)", (user.username, hashed_password, user.role))
        conn.commit()

        cur.close()
        conn.close()
    
    def update_user(self, user: UserEdit):
        conn = psycopg2.connect(
            host=DB_HOSTNAME,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )

        cur = conn.cursor()
        cur.execute("UPDATE users SET username=%s, password=%s,  WHERE id=%s", (user.username, user.password, user.role, user.user_id))
        conn.commit()

        cur.close()
        conn.close()

