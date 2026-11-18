import uvicorn
from fastapi import FastAPI

from src.config import port

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("src.app:app", port=port, reload=True, reload_dirs=["src"])
