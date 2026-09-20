import os
from dotenv import load_dotenv

# Load variables from backend/.env into the process environment.
# This must run before anything else reads os.environ.
load_dotenv()


class Settings:
    """
    Centralized access to environment-driven configuration.

    We read these once at import time rather than scattering
    os.environ.get() calls throughout the codebase — this makes it
    obvious what configuration the app depends on, all in one place.
    """

    DATABASE_URL: str = os.environ["DATABASE_URL"]
    APP_ENV: str = os.environ.get("APP_ENV", "development")
    DEBUG: bool = os.environ.get("DEBUG", "false").lower() == "true"

    # Auth / JWT settings — required now that login issues real tokens.
    JWT_SECRET: str = os.environ["JWT_SECRET"]
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))


settings = Settings()
