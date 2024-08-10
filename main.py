from fastapi import FastAPI
from api.router import api_router
from core.config import settings
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse
from sqlalchemy import text
from api.depends.get_db import get_db
from logging_config import LOGGING_CONFIG

import asyncio
import logging


app = app = FastAPI(
    title="Sound Light",
    description="Sound Light의 API 문서입니다",
    version="v2.0"
)

app.include_router(api_router)


logger = logging.getLogger("uvicorn")



#### logging middleware ####
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logging.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)

        if isinstance(response, Response) and not isinstance(
            response, StreamingResponse
        ):
            if isinstance(response.content, bytes):
                try:
                    body = response.content.decode()
                    logging.info(f"Response body: {body}")
                except Exception as e:
                    logging.error(f"Could not log response body: {e}")

        logging.info(f"Response: {response.status_code}")
        return response


#### add CORS middleware ####
app.add_middleware(
    CORSMiddleware, 
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#### checking db connection ####
def check_db_connection(db=None):
    if not db:
        gen = get_db()
        db = next(gen)
        try:
            db.execute(text("SELECT 1"))
        finally:
            next(gen, None)
    else:
        db.execute(text("SELECT 1"))


async def startup_db_check():
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, check_db_connection)


@app.on_event("startup")
async def on_startup():
    logging.info("Trying DB connection before stating...")
    await startup_db_check()
    logging.info(f"DB connected!")
