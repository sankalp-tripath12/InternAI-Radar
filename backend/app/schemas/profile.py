import uuid
from pydantic import BaseModel, ConfigDict


class ProfileUpdate(BaseModel):
    full_name: str
    location: str | None = None
    target_role: str | None = None
    graduation_year: int | None = None


class ProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    full_name: str
    location: str | None
    target_role: str | None
    graduation_year: int | None
