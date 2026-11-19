"""Request and response bodies for /items, based on FastAPI's Request Body tutorial."""

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class ItemCreate(ItemBase):
    """Body of POST /items."""


class ItemUpdate(ItemBase):
    """Body of PUT /items/{item_id}, which replaces the whole item."""


class ItemResponse(ItemBase):
    """An item as returned by the API."""

    id: str
