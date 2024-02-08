import pymongo
import time
from .constants import db_user, db_pass

# Maximum time to wait for the database connection (3 minutes)
DB_CONNECTION_TIMEOUT = 180  # in seconds

def connect_to_database():
    start_time = time.time()
    while True:
        try:
            client = pymongo.MongoClient(
                f"mongodb+srv://{db_user}:{db_pass}@cluster0.ds5ggbq.mongodb.net/?retryWrites=true&w=majority",
                serverSelectionTimeoutMS=DB_CONNECTION_TIMEOUT * 1000
            )
            return client
        except pymongo.errors.ServerSelectionTimeoutError:
            if time.time() - start_time > DB_CONNECTION_TIMEOUT:
                raise TimeoutError("Connection to the database timed out.")
            time.sleep(0.2)

client = connect_to_database()

def get_db():
    return client.get_database("starter_template")


# authentication
import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = "SECRET"

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_id):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, minutes=30),
            "iat": datetime.utcnow(),
            "sub": user_id,
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Signature has expired")
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail="Invalid token")

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)