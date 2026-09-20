import uuid

import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.mark.asyncio
async def test_register_creates_user_and_hides_password():
    """
    Registering with a new email should succeed (201) and the response
    must NOT contain the password or hash in any form.
    """
    unique_email = f"test-{uuid.uuid4()}@example.com"
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post(
            "/api/v1/auth/register",
            json={"email": unique_email, "password": "testpassword123"},
        )

    assert response.status_code == 201
    body = response.json()
    assert body["email"] == unique_email
    assert "id" in body
    assert "password" not in body
    assert "hashed_password" not in body


@pytest.mark.asyncio
async def test_register_rejects_duplicate_email():
    """
    Registering the same email twice should fail the second time
    with a 409 Conflict, not a raw 500 database error.
    """
    unique_email = f"test-{uuid.uuid4()}@example.com"
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        first = await client.post(
            "/api/v1/auth/register",
            json={"email": unique_email, "password": "testpassword123"},
        )
        second = await client.post(
            "/api/v1/auth/register",
            json={"email": unique_email, "password": "differentpassword456"},
        )

    assert first.status_code == 201
    assert second.status_code == 409
