import uuid

from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base

# The association table for the many-to-many User <-> Skill relationship.
# This is deliberately a plain Table, not a full model class, because it
# holds no data of its own beyond the two foreign keys — just the pairing.
user_skills = Table(
    "user_skills",
    Base.metadata,
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("skill_id", UUID(as_uuid=True), ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True),
)


class Skill(Base):
    """
    A single reusable skill (e.g. "Python", "Docker").

    Kept as its own table with a UNIQUE name so the same skill is
    never duplicated across users — this becomes important once the
    Matching Engine (Phase 4) needs to compare a user's skills against
    an opportunity's required skills reliably.
    """

    __tablename__ = "skills"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
