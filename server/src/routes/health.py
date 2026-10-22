from datetime import UTC, datetime

from fastapi import APIRouter, Response, status

from src.schemas.health import HealthResponse
from src.services.health import check_database

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
def health(response: Response) -> HealthResponse:
    database = check_database()

    if database == "disconnected":
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return HealthResponse(
        status="error" if database == "disconnected" else "ok",
        database=database,
        timestamp=datetime.now(UTC),
    )
