from fastapi import FastAPI
from .routers import items, users, models

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

app.include_router(items.router)
app.include_router(users.router)
app.include_router(models.router)