import logging

from fastapi import FastAPI

from .logging_setup import setup_logging
from .settings import settings

setup_logging(settings.log_level)
log = logging.getLogger("app")

app = FastAPI(title=settings.app_name, version=settings.app_version)


@app.on_event("startup")
def on_startup() -> None:
    log.info("app_startup")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/ready")
def ready() -> dict:
    return {"status": "ready"}


@app.get("/version")
def version() -> dict:
    return {
        "app": settings.app_name,
        "env": settings.app_env,
        "version": settings.app_version,
    }
