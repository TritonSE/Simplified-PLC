"""Default settings so the tests run without a backend/.env file or a running MongoDB."""

import os

os.environ.setdefault("MONGODB_URI", "mongodb://localhost:27017/simplified-plc-test")
os.environ.setdefault("FRONTEND_ORIGIN", "http://localhost:3000")
