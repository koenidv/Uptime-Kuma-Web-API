from pydantic import AnyHttpUrl, BaseSettings
from fastapi.logger import logger as fast_api_logger
from typing import List
import logging
import os

logger = logging.getLogger("gunicorn.error")
fast_api_logger.handlers = logger.handlers


class Settings(BaseSettings):
    PROJECT_NAME: str = "Uptime-Kuma-API"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    KUMA_SERVER: str = os.environ.get("KUMA_SERVER")
    KUMA_USERNAME: str = os.environ.get("KUMA_USERNAME")
    KUMA_PASSWORD: str = os.environ.get("KUMA_PASSWORD")

    API_KEY: str = os.environ.get("API_KEY")

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
