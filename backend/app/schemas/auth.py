import uuid
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class RegisterRequest(BaseModel):
    """What the client must send to register. Pydantic validates
    email format and enforces a minimum password length automatically —
    we don't have to hand-write that validation ourselves."""
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class LoginRequest(BaseModel):
    """What the client sends to log in. No length constraint here —
    we're checking an EXISTING password, not creating a new one, so
    we don't want to reject a valid (already-registered) password
    just because our current rules changed since they signed up."""
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """What we return after a successful login."""
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    """What we send back after registration or when fetching the
    current user. Deliberately excludes hashed_password — this schema
    is the guarantee that a password hash can never accidentally leak
    into an API response."""
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    email: EmailStr
