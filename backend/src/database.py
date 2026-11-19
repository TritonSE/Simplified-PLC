"""MongoDB connection, opened and closed with the app's lifespan."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Annotated, Any

from fastapi import Depends, FastAPI, Request
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

from src.config import settings

DEFAULT_DATABASE_NAME = "simplified-plc"


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Connect to MongoDB when the app starts and disconnect when it stops."""
    client: AsyncMongoClient[dict[str, Any]] = AsyncMongoClient(settings.MONGODB_URI)
    app.state.database = client.get_default_database(default=DEFAULT_DATABASE_NAME)
    try:
        yield
    finally:
        await client.close()


async def get_database(request: Request) -> AsyncDatabase[dict[str, Any]]:
    """Return the app's database. Use it through the Database dependency."""
    database: AsyncDatabase[dict[str, Any]] = request.app.state.database
    return database


Database = Annotated[AsyncDatabase[dict[str, Any]], Depends(get_database)]
