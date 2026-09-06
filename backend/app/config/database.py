from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.config.settings import settings

# The engine manages the actual pool of connections to Postgres.
# echo=settings.DEBUG prints every SQL statement to the console,
# which is useful now and will get noisy once we have real traffic.
engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG)

# async_sessionmaker gives us a factory for creating new DB sessions
# per-request, rather than sharing one session across the whole app.
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncSession:
    """
    FastAPI dependency that yields a database session for a single request,
    and guarantees it's closed afterward even if the request raises an error.
    """
    async with AsyncSessionLocal() as session:
        yield session
