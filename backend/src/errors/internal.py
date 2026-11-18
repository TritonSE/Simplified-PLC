from typing import ClassVar

from src.errors.errors import CustomError

NO_APP_PORT = "Could not find app port env variable"


class InternalError(CustomError):
    NO_APP_PORT: ClassVar[InternalError]


InternalError.NO_APP_PORT = InternalError(0, 500, NO_APP_PORT)
