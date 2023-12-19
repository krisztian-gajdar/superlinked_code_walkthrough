from fastapi import FastAPI
from tier_backend.api.url import router as url_router
from tier_backend.db.base import init_db
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from tier_backend.core.config import Settings
import logging

logger = logging.getLogger(__name__)
settings = Settings()

app = FastAPI(title=settings.title)
app.add_middleware(DBSessionMiddleware, db_url=settings.db_url)
origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()
app.include_router(url_router)
logger.info("Application started.")


@app.get("/")
async def root():
    return {"message": "See /docs for endpoint documentation"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app", host="0.0.0.0", port=80, log_level="debug", debug=True, workers=1
    )
