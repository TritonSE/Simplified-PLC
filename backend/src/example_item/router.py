from fastapi import APIRouter, status

from src.database import Database
from src.example_item import service
from src.example_item.exceptions import ItemNotFound
from src.example_item.schemas import ItemCreate, ItemResponse, ItemUpdate

router = APIRouter(prefix="/items", tags=["items"])


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_item(data: ItemCreate, database: Database) -> ItemResponse:
    return await service.create(database, data)


@router.get("")
async def get_items(database: Database) -> list[ItemResponse]:
    return await service.get_all(database)


@router.get("/{item_id}")
async def get_item(item_id: str, database: Database) -> ItemResponse:
    item = await service.get_by_id(database, item_id)
    if item is None:
        raise ItemNotFound()
    return item


@router.put("/{item_id}")
async def update_item(item_id: str, data: ItemUpdate, database: Database) -> ItemResponse:
    item = await service.update(database, item_id, data)
    if item is None:
        raise ItemNotFound()
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, database: Database) -> None:
    if not await service.delete(database, item_id):
        raise ItemNotFound()
