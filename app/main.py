from fastapi import FastAPI
from .routers import items, users

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

app.include_router(items.router)
app.include_router(users.router)