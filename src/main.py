from fastapi import FastAPI
from src.users.router import router as router_users
from src.auth.router import router as router_auth

app = FastAPI()

app.include_router(router_auth)
app.include_router(router_users)
