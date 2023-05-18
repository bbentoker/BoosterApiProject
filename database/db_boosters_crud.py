import psycopg2
import jwt
import hmac
from config import *
import bcrypt
from validations.user_validation import UserLogin
from validations.booster_validation import Booster


class Boosters_CRUD:

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

    def create_user(self, user: Booster):
        conn = psycopg2.connect(
            host=DB_HOSTNAME,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )

        password  = bytes(user.password, 'utf-8')
        hashed_password = hmac.new(bytes(PWD_HASH_SECRET, 'utf-8'), password, digestmod='sha256').hexdigest()

        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password, role, about) VALUES (%s,%s,%s,%s)", (user.username, hashed_password, user.user_role, user.about))
        cur.execute("SELECT id FROM users WHERE username = %s", (user.username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO booster_details (user_id, boost_type, server, rank, role, details, price) VALUES (%s,%s,%s,%s,%s,%s,%s)", (user_id, user.boost_type, user.server, user.rank, user.game_role, user.details, user.price))

        conn.commit()
        cur.close()
        conn.close()
    
    def get_all_boosters(self):
        conn = psycopg2.connect(
        host=DB_HOSTNAME,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD
    )

        cur = conn.cursor()

        # Retrieve all rows from booster_details table
        cur.execute("SELECT * FROM booster_details")

        boosters = []
        for row in cur.fetchall():
            # For each row, retrieve the corresponding user from the users table
            user_id = row[1]
            cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            user_row = cur.fetchone()

            # Create a dictionary representing the combined booster and user record
            booster_and_user = {
                "booster_id": row[0],
                "user_id": user_id,
                "boost_type": row[2],
                "server": row[3],
                "rank": row[4],
                "role": row[5],
                "details": row[6],
                "price": row[7],
                "username": user_row[1],
                "about": user_row[4],
            }
            # Append the combined record to the list of boosters
            boosters.append(booster_and_user)

        cur.close()
        conn.close()

        return boosters