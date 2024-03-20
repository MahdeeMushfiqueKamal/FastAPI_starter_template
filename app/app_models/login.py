from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "user",
                "password": "1234"
            }
        }
