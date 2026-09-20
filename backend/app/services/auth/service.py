from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.services.auth.password import hash_password


class EmailAlreadyRegisteredError(Exception):
    """Raised when someone tries to register with an email already in use."""
    pass


async def register_user(db: AsyncSession, email: str, password: str) -> User:
    """
    Create a new user account.

    We check for an existing email BEFORE inserting, which handles the
    common case with a clean error message. But two requests for the
    same email could both pass that check before either commits (a
    race condition), so we ALSO catch the database's own unique
    constraint violation as a backup — this guarantees we can never
    end up with duplicate emails, and still return our clean error
    type either way, not a raw database exception.
    """
    existing = await db.execute(select(User).where(User.email == email))
    if existing.scalar_one_or_none() is not None:
        raise EmailAlreadyRegisteredError(f"Email {email} is already registered")

    user = User(email=email, hashed_password=hash_password(password))
    db.add(user)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise EmailAlreadyRegisteredError(f"Email {email} is already registered")

    await db.refresh(user)  # populate server-generated fields like id, created_at
    return user
