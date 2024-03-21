# app/routers/example.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"success": True,"message": "Hello, World!"}


@router.post("/")
def read_root_post(data: dict):
    return {
        "success": True,
        "data": data
    }
