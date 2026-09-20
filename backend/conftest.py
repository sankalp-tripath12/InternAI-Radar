import pytest

from app.config.database import engine


@pytest.fixture(autouse=True)
async def dispose_engine_after_test():
    """
    Our database engine is a module-level singleton, created once at
    import time. Its connection pool binds to whichever asyncio event
    loop exists when a connection is first opened. Without this fixture,
    a connection opened during one test remains tied to that test's loop,
    and the next test (running under pytest-asyncio's session-scoped loop)
    would try to reuse it and fail with "another operation is in progress".

    Disposing the pool after every test forces SQLAlchemy to open a fresh
    connection next time, bound to whatever loop is currently active.
    This is the standard fix for combining a long-lived async engine with
    pytest-asyncio.
    """
    yield
    await engine.dispose()
