from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.services.auth.password import hash_password, verify_password


class EmailAlreadyRegisteredError(Exception):
    """Raised when someone tries to register with an email already in use."""
    pass


class InvalidCredentialsError(Exception):
    """Raised when login email/password don't match any account.
    Deliberately the SAME error for 'no such email' and 'wrong password' —
    telling an attacker which one is wrong would confirm whether a given
    email is registered at all, which is information we shouldn't leak."""
    pass


async def register_user(db: AsyncSession, email: str, password: str) -> User:
    """
    Create a new user account.

    We check for an existing email BEFORE inserting, which handles the
    common case with a clean error message. But two requests for the
    same email could both pass that check before either commits (a
    race condition), so we ALSO catch the database's own unique
    constraint violation as a backup.
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

    await db.refresh(user)
    return user


async def authenticate_user(db: AsyncSession, email: str, password: str) -> User:
    """
    Verify login credentials and return the matching User.

    Raises InvalidCredentialsError for both a non-existent email AND
    a wrong password — see the class docstring for why these are
    deliberately indistinguishable to the caller.
    """
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if user is None or not verify_password(password, user.hashed_password):
        raise InvalidCredentialsError("Invalid email or password")

    return user
