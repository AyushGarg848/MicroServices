from fastapi import APIRouter, Query, Cookie, Depends
from typing import Annotated
from pydantic import BaseModel

router = APIRouter()

def query_extractor(q: str | None = None):
    return q

def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[str | None, Cookie()] = None,
):
    if not q:
        return last_query
    return q

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# @router.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixed query$")] = None):
#     results = {"items": ["Foo", "Bar"]}
#     if q:
#         results.update({"q": q})
#     return results

@router.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
):
    return {"q_or_cookie": query_or_default}

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