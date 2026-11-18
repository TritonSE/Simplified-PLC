import os

from dotenv import load_dotenv

from src.errors import InternalError

load_dotenv()

if not os.environ.get("PORT"):
    raise InternalError.NO_APP_PORT
port = int(os.environ["PORT"])

__all__ = ["port"]
