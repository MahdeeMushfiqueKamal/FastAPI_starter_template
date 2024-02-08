from fastapi import APIRouter
from ..app_models.login import Login

router = APIRouter()

@router.post("/login")
def read_example(login: Login):
    return {"success": True,"message": f"Hello, {login.username}!"}
