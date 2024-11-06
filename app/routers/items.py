from fastapi import APIRouter

router = APIRouter()

@router.get("/items/{item_id}")
async def read_items(item_id:int):
    return {"items_id": item_id}
