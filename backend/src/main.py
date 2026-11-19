from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.database import lifespan
from src.example_item.router import router as items_router

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items_router)


@app.get("/")
async def root() -> dict[str, str]:
    """Return a hello world message, from FastAPI's First Steps tutorial."""
    return {"message": "Hello World"}
