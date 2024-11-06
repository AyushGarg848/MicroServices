from fastapi import APIRouter
from enum import Enum

class ModelName(str, Enum):
    nokia = "nokia"
    ericsson = "ericsson"
    samsung= "samsung"

router = APIRouter()

@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.nokia:
        return {"model_name": model_name, "message": "Welcome to Nokia!"}
    if model_name.value == "ericsson":
        return {"model_name": model_name, "message": "Welcome to Ericsson!"}
    return {"model_name": model_name, "message": "Welcome to Samsung!"}