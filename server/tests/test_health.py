import db
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health_ok_when_database_disabled(monkeypatch):
    monkeypatch.setattr(db, "pool", None)

    res = client.get("/api/health")

    assert res.status_code == 200
    assert res.json()["status"] == "ok"
    assert res.json()["database"] == "not_configured"


def test_unknown_route_returns_404():
    assert client.get("/api/does-not-exist").status_code == 404
