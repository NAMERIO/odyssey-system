from datetime import datetime
from typing import Literal

from pydantic import BaseModel

DatabaseStatus = Literal["connected", "disconnected", "not_configured"]


class HealthResponse(BaseModel):
    status: Literal["ok", "error"]
    database: DatabaseStatus
    timestamp: datetime
