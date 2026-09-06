import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.mark.asyncio
async def test_health_check_returns_ok():
    """
    Confirms the /health endpoint responds successfully and reports
    a working database connection. This is our smoke test for Phase 0 —
    if this fails, the whole stack (API + DB) isn't wired up correctly.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "connected"}
