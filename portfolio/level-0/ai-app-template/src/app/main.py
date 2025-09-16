import logging
import uuid

import httpx
from core.retry import retry
from fastapi import FastAPI, Query, Request
from fastapi.responses import JSONResponse

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


@app.get("/echo")
def echo(q: str = Query(..., min_length=5, max_length=50)) -> dict:
    return {"echo": q}


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


class DemoError(Exception): ...


@app.get("/boom")
def boom() -> dict:
    raise DemoError("kaboom")


@app.exception_handler(DemoError)
def handle_demo_error(_: Request, exc: DemoError) -> JSONResponse:
    return JSONResponse(status_code=400, content={"error": str(exc)})


async def httpbin() -> dict:
    async with httpx.AsyncClient(timeout=5) as client:
        r = await client.get("https://httpbin.org/get")
        r.raise_for_status()
        data = r.json()
        return {"origin": data.get("origin", "unknown")}


@app.get("/httpbin")
async def _call():
    async with httpx.AsyncClient(timeout=5) as client:
        return (await client.get("https://httpbin.org/get")).json()
    data = await retry(_call)


@app.middleware("http")
async def add_request_id(request: Request, call_next):
    req_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    response = await call_next(request)
    response.headers["X-Request-ID"] = req_id
    return response
