"""Configuration for the real-time sector capital-flow service."""

import os
from pathlib import Path

from dotenv import load_dotenv


BACKEND_DIR = Path(__file__).resolve().parent


def load_environment(env_file: Path = BACKEND_DIR / ".env") -> bool:
    """Load backend settings without replacing deployment-level variables."""
    return load_dotenv(env_file, override=False)


# Run before service singletons read os.environ.
load_environment()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8100"))


def env_path(name: str, default: Path) -> Path:
    """Read a path setting, resolving relative values from the backend directory."""
    value = os.getenv(name)
    if not value:
        return default
    path = Path(value).expanduser()
    if path.is_absolute():
        return path
    return BACKEND_DIR / path

REQUEST_TIMEOUT = 10.0
MAX_RETRIES = 2
RETRY_DELAY = 500

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    ),
    "Referer": "https://data.eastmoney.com/",
}

EASTMONEY_SECTOR_URL = "https://push2delay.eastmoney.com/api/qt/clist/get"
EASTMONEY_PUSH_URL = "https://push2.eastmoney.com/api/qt/clist/get"
EASTMONEY_SECTOR_CAPITAL_FLOW_URL = (
    "https://push2.eastmoney.com/api/qt/stock/fflow/kline/get"
)
EASTMONEY_SECTOR_CAPITAL_FLOW_FALLBACK_URL = (
    "https://push2delay.eastmoney.com/api/qt/stock/fflow/kline/get"
)
EASTMONEY_SECTOR_DAILY_FLOW_URL = (
    "https://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get"
)
EASTMONEY_SECTOR_FLOW_SNAPSHOT_URL = (
    "https://push2.eastmoney.com/api/qt/ulist.np/get"
)
EASTMONEY_SECTOR_FLOW_SNAPSHOT_FALLBACK_URL = (
    "https://push2delay.eastmoney.com/api/qt/ulist.np/get"
)
EASTMONEY_STOCK_SEARCH_URL = "https://searchapi.eastmoney.com/api/suggest/get"
EASTMONEY_STOCK_FLOW_SNAPSHOT_URL = "https://push2.eastmoney.com/api/qt/ulist.np/get"
EASTMONEY_STOCK_FLOW_SNAPSHOT_FALLBACK_URL = (
    "https://push2delay.eastmoney.com/api/qt/ulist.np/get"
)
