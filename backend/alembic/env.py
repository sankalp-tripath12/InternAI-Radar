import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

# Import our Base and every model, so Alembic's autogenerate can see
# the full picture of what tables SHOULD exist. Every new model we
# add later must be imported here too, or Alembic won't know about it.
from app.models.base import Base
from app.models.user import User  # noqa: F401
from app.models.profile import Profile  # noqa: F401
from app.models.education import Education  # noqa: F401
from app.models.skill import Skill, user_skills  # noqa: F401
from app.models.resume import Resume  # noqa: F401

from app.config.settings import settings

config = context.config

# Inject our real DATABASE_URL from settings, so we have exactly
# one source of truth for the connection string (not duplicated
# between .env and alembic.ini).
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Generate SQL scripts without a live DB connection (rarely used by us, but standard Alembic scaffolding)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """
    The path we actually use: connect to the real (async) database
    and run migrations against it directly.
    """
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
