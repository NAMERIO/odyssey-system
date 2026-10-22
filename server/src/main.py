from contextlib import asynccontextmanager

import db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import CLIENT_URL
from src.routes import health

API_PREFIX = "/api"


@asynccontextmanager
async def lifespan(_: FastAPI):
    if db.pool:
        db.pool.open(wait=False)
    yield
    if db.pool:
        db.pool.close()


app = FastAPI(
    title="Odyssey API",
    lifespan=lifespan,
    docs_url=f"{API_PREFIX}/docs",
    openapi_url=f"{API_PREFIX}/openapi.json",
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CLIENT_URL],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix=API_PREFIX)
