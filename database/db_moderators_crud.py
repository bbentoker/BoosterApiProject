import psycopg2
import jwt
import hmac
from config import *
import bcrypt
from validations.moderators_validation import Moderator, UserLogin


class Moderators_CRUD:

    def get_user(self, user: UserLogin):
        conn = psycopg2.connect(
            host=DB_HOSTNAME,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )

        print(f"user object: {user} and type: {type(user)}")

        user_password = bytes(user['password'], 'utf-8')
        hashed_password = hmac.new(bytes(PWD_HASH_SECRET, 'utf-8'), user_password, digestmod='sha256').hexdigest()
        print(hashed_password)

        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user['username'], hashed_password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user

    def create_user(self, user: Moderator):
        conn = psycopg2.connect(
            host=DB_HOSTNAME,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )

        password  = bytes(user.password, 'utf-8')
        hashed_password = hmac.new(bytes(PWD_HASH_SECRET, 'utf-8'), password, digestmod='sha256').hexdigest()

        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password, role) VALUES (%s,%s,%s)", (user.username, hashed_password, 'moderator'))
        conn.commit()

        cur.close()
        conn.close()
