import db

from src.schemas.health import DatabaseStatus


def check_database() -> DatabaseStatus:
    if not db.pool:
        return "not_configured"
    return "connected" if db.ping() else "disconnected"
