import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from settings.logger import LoggerSettings

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
    log: LoggerSettings = LoggerSettings()

def _register_environ(settings: BaseSettings):
    for field_name, value in settings:
        if isinstance(value, BaseSettings):
            _register_environ(value)
        else:
            os.environ[field_name.upper()] = str(value)

@lru_cache(maxsize=1)
def get_settings(into_env: bool = False) -> BaseSettings:
    settings = Settings()
    if into_env:
        _register_environ(settings)
    return settings