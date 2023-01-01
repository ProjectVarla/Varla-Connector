from ipaddress import IPv4Address
from os import getenv
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings, validator

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "Varla-Connector"

    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = 360
    GATEWAY_TIMEOUT: int = 59

    BACKUP_SERVICE_URL: Optional[str]
    TASKS_SERVICE_URL: Optional[str]
    NOTIFICATION_CORE_URL: Optional[str]
    ORCHESTRATOR_INFRASTRUCTURE_URL: Optional[str]

    DEFAULT_CHANNEL: Optional[str] = "FileManager"

    GATEWAY_HOST: str
    GATEWAY_PORT: int

    @validator("GATEWAY_PORT", always=True)
    def gateway_port_validator(cls, v):
        return int(getenv("GATEWAY_PORT"))

    @validator("GATEWAY_HOST", always=True)
    def gateway_host_validator(cls, v):
        return str(IPv4Address(getenv("GATEWAY_HOST")))

    @validator("BACKUP_SERVICE_URL", always=True)
    def backup_service_url_validator(cls, v):
        return getenv("BACKUP_SERVICE_URL")

    @validator("TASKS_SERVICE_URL", always=True)
    def tasks_service_url_validator(cls, v):
        return getenv("TASKS_SERVICE_URL")

    @validator("NOTIFICATION_CORE_URL", always=True)
    def notification_core_url_validator(cls, v):
        return getenv("NOTIFICATION_CORE_URL")

    @validator("ORCHESTRATOR_INFRASTRUCTURE_URL", always=True)
    def orchestrator_infrastructure_url_validator(cls, v):
        return getenv("ORCHESTRATOR_INFRASTRUCTURE_URL")


settings = Settings()
