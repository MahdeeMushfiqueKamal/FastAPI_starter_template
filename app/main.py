from fastapi import FastAPI
from .routers import hello, login

app = FastAPI()

app.include_router(hello.router)
app.include_router(login.router)
