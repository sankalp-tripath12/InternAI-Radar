import uuid
from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError

from app.config.settings import settings


def create_access_token(user_id: uuid.UUID) -> str:
    """
    Create a signed JWT containing only the user's id and an expiration.

    We deliberately keep the payload minimal — no email, no other
    personal data — since JWT payloads are readable by anyone who has
    the token (they're signed, not encrypted). The signature (using
    JWT_SECRET) is what makes the token trustworthy, not secrecy of
    its contents.
    """
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": str(user_id), "exp": expire}
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


def decode_access_token(token: str) -> uuid.UUID | None:
    """
    Verify a token's signature and expiration, and extract the user id.

    Returns None on ANY failure (expired, tampered, malformed) rather
    than raising — callers decide how to respond (typically a 401),
    keeping this function focused purely on the crypto/parsing concern.
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        return uuid.UUID(payload["sub"])
    except (JWTError, KeyError, ValueError):
        return None
