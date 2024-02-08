from fastapi import APIRouter, Depends, HTTPException
from ..app_models.login import Login
from ..utils import AuthHandler, get_db

router = APIRouter()
db = get_db()
auth_handler = AuthHandler()

@router.post("/login", tags=["Authentication"])
async def read_example(login: Login):
    user = db.users.find_one({"username": login.username}) 
    if user is None:
        raise HTTPException(
        status_code=400,
        detail="Incorrect email or password",
    )
    hashed_pass = user["password"]
    if auth_handler.verify_password(login.password, hashed_pass):
        token = auth_handler.encode_token(login.username)
        return {"token": token, "success": True}
    
    raise HTTPException(
        status_code=400,
        detail="Incorrect email or password",
    )


@router.get("/check_authentication", tags=["Authentication"])
def check_authentication(user_id=Depends(auth_handler.auth_wrapper)):
    if user_id:
        return {"success": True, "message": "User is authenticated"}
