from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str
    
    class Config:
        schema_extra = {
            "example": {
                "username": "user",
                "password": "1234"
            }
        }
