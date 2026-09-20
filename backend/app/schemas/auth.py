import uuid
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class RegisterRequest(BaseModel):
    """What the client must send to register. Pydantic validates
    email format and enforces a minimum password length automatically —
    we don't have to hand-write that validation ourselves."""
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserResponse(BaseModel):
    """What we send back after registration. Deliberately excludes
    hashed_password — this schema is the guarantee that a password
    hash can never accidentally leak into an API response."""
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    email: EmailStr
