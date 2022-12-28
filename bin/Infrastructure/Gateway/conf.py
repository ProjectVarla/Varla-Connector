from os import getenv

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

TASKS_SERVICE_URL = getenv("TASKS_SERVICE_URL")
BACKUP_SERVICE_URL = getenv("BACKUP_SERVICE_URL")
NOTIFICATION_CORE_URL = getenv("NOTIFICATION_CORE_URL")


class Settings(BaseSettings):
    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = 360
    TASKS_SERVICE_URL: str = str(TASKS_SERVICE_URL)
    BACKUP_SERVICE_URL: str = str(BACKUP_SERVICE_URL)
    NOTIFICATION_CORE_URL: str = str(NOTIFICATION_CORE_URL)

    GATEWAY_TIMEOUT: int = 59


settings = Settings()
