from fastapi import APIRouter, Query
from typing import Annotated
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@router.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixed query$")] = None):
    results = {"items": ["Foo", "Bar"]}
    if q:
        results.update({"q": q})
    return results

@router.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@router.post("/items/")
async def create_item(item: Item):
    if item.tax is None:
        item.tax = item.price * 0.18
    return item.tax

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result