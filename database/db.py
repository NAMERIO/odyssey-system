from pathlib import Path

import hjson
from psycopg import Error as DatabaseError
from psycopg.conninfo import make_conninfo
from psycopg_pool import ConnectionPool, PoolTimeout

CONFIG_PATH = Path(__file__).resolve().parent.parent / "odyssey-config.hjson"
LOCAL_URL = "postgresql://postgres:postgres@127.0.0.1:54322/postgres"


def load_settings() -> dict:
    if not CONFIG_PATH.exists():
        return {}
    return hjson.loads(CONFIG_PATH.read_text("utf-8")).get("database", {})


settings = load_settings()
url = settings.get("url", LOCAL_URL)

pool = (
    ConnectionPool(make_conninfo(url, connect_timeout=5), open=False)
    if settings.get("enabled", False)
    else None
)


def ping() -> bool:
    try:
        with pool.connection(timeout=2) as conn:
            conn.execute("SELECT 1")
        return True
    except (DatabaseError, PoolTimeout):
        return False
