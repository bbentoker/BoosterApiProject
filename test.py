import jwt
from config import *
import time
token = jwt.encode({"user_id": 1, "role": "moderator", "expire_time": int(time.time() - 500)}, JWT_SECRET, algorithm=JWT_ALGORITHM)
print(token)