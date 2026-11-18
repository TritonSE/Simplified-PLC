from collections.abc import Callable
from types import ModuleType

import pytest
from fastapi.testclient import TestClient

from src.errors import InternalError


def test_app_serves_api_docs(
    monkeypatch: pytest.MonkeyPatch, load_module: Callable[[str], ModuleType]
) -> None:
    monkeypatch.setenv("PORT", "8000")
    app = load_module("src.app").app

    with TestClient(app) as client:
        assert client.get("/docs").status_code == 200
        assert client.get("/openapi.json").status_code == 200


def test_config_without_port_raises_no_app_port(
    monkeypatch: pytest.MonkeyPatch, load_module: Callable[[str], ModuleType]
) -> None:
    monkeypatch.delenv("PORT", raising=False)

    with pytest.raises(InternalError) as exc_info:
        load_module("src.config")

    assert exc_info.value is InternalError.NO_APP_PORT
    assert exc_info.value.message == "Could not find app port env variable"
