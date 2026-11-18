import importlib
import sys
from collections.abc import Callable
from types import ModuleType

import pytest


@pytest.fixture
def load_module(monkeypatch: pytest.MonkeyPatch) -> Callable[[str], ModuleType]:
    """Return a loader that imports a fresh copy of a module without reading any .env file."""
    monkeypatch.setenv("PYTHON_DOTENV_DISABLED", "1")
    for name in ("src.app", "src.config"):
        monkeypatch.delitem(sys.modules, name, raising=False)
    return importlib.import_module
