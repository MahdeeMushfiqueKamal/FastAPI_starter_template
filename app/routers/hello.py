# app/routers/example.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"success": True,"message": "Hello, World!"}
