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


settings = Settings()
