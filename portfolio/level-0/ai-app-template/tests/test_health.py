import logging

from fastapi.testclient import TestClient

from app.main import app


def test_health_ok() -> None:
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_echo_ok() -> None:
    from fastapi.testclient import TestClient

    from app.main import app

    client = TestClient(app)
    r = client.get("/echo", params={"q": "hello"})
    assert r.status_code == 200 and r.json() == {"echo": "hello"}

    r = client.get("/echo?q=12")
    assert r.status_code == 422


def test_ready_ok() -> None:
    client = TestClient(app)
    r = client.get("/ready")
    assert r.status_code == 200
    assert r.json() == {"status": "ready"}


def test_version_ok() -> None:
    client = TestClient(app)
    r = client.get("/version")
    assert r.status_code == 200
    assert r.json() == {
        "app": "ai-app-template",
        "env": "local",
        "version": "0.1.0",
    }


def test_startup_event(caplog) -> None:
    with caplog.at_level(logging.INFO, logger="app"):
        with TestClient(app):
            pass
    assert any(record.message == "app_startup" for record in caplog.records)
