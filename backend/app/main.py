from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import get_db

app = FastAPI(title="InternAI Radar API")


@app.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    """
    Liveness + database connectivity check.

    Runs a trivial query against Postgres so we know not just that
    the API process is alive, but that it can actually reach the database.
    """
    await db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "connected"}
