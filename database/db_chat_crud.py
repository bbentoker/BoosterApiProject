import psycopg2
from config import *
from validations.chat_validation import MessageValidation

class CHAT_CRUD:
    def create(self,message: MessageValidation):
        conn = psycopg2.connect(
            host=DB_HOSTNAME,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
            )

        cur = conn.cursor()
        cur.execute("INSERT INTO messages(sender_id, receiver_id, message, read) VALUES(%s, %s, %s, %s)", (message.client_id, message.receiver_id, message.message, False))
        cur.close()
        conn.close()

    






  


