from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .routers import items, users, models

app = FastAPI()

class CustomException(Exception):
    def __init__(self, name: str, status_code: int):
        self.name = name
        self.status_code = status_code

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request,exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"Oops! {exc.name} did something!!"}
    )

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id != "foo":
        raise CustomException(
            status_code=418,
            name=item_id
        )
    return {"item": "foo"}

app.include_router(items.router)
app.include_router(users.router)
app.include_router(models.router)