from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    The shared base class every SQLAlchemy model inherits from.

    Keeping this in its own file (rather than defining it inside
    user.py) matters once we have many models — they all need to
    import the SAME Base instance so Alembic can see every table
    when it compares our models against the database.
    """
    pass
