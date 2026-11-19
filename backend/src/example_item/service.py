"""MongoDB queries for the items collection."""

from typing import Any

from bson import ObjectId
from pymongo import ReturnDocument
from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.database import AsyncDatabase

from src.example_item.schemas import ItemCreate, ItemResponse, ItemUpdate

COLLECTION_NAME = "items"


def _collection(database: AsyncDatabase[dict[str, Any]]) -> AsyncCollection[dict[str, Any]]:
    return database[COLLECTION_NAME]


def _to_response(document: dict[str, Any]) -> ItemResponse:
    return ItemResponse(id=str(document.pop("_id")), **document)


async def create(database: AsyncDatabase[dict[str, Any]], data: ItemCreate) -> ItemResponse:
    """Insert a new item and return it with its id."""
    document = data.model_dump()
    await _collection(database).insert_one(document)
    return _to_response(document)


async def get_all(database: AsyncDatabase[dict[str, Any]]) -> list[ItemResponse]:
    """Return every item."""
    return [_to_response(document) async for document in _collection(database).find()]


async def get_by_id(database: AsyncDatabase[dict[str, Any]], item_id: str) -> ItemResponse | None:
    """Return the item with item_id, or None if there is none or the id is not valid."""
    if not ObjectId.is_valid(item_id):
        return None
    document = await _collection(database).find_one({"_id": ObjectId(item_id)})
    return _to_response(document) if document else None


async def update(
    database: AsyncDatabase[dict[str, Any]], item_id: str, data: ItemUpdate
) -> ItemResponse | None:
    """Replace the item with item_id and return it, or None if it does not exist."""
    if not ObjectId.is_valid(item_id):
        return None
    document = await _collection(database).find_one_and_replace(
        {"_id": ObjectId(item_id)}, data.model_dump(), return_document=ReturnDocument.AFTER
    )
    return _to_response(document) if document else None


async def delete(database: AsyncDatabase[dict[str, Any]], item_id: str) -> bool:
    """Delete the item with item_id and return whether it existed."""
    if not ObjectId.is_valid(item_id):
        return False
    result = await _collection(database).delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count == 1
