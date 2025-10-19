from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

class LoggerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    LOG_YAML: str = "basic.yaml"
    LOG_DIR: str = "src/logger/logs"
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"