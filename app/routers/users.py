from fastapi import APIRouter

router = APIRouter()

@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@router.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    item.update({"q": q})
    if short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item