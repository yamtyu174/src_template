import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from settings.logger import LoggerSettings
from exceptions import exception_handler, ConfigLoadError

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
    PYTHONPATH: str = "src"
    log: LoggerSettings = LoggerSettings()

def _register_environ(settings: BaseSettings):
    for field_name, value in settings:
        if isinstance(value, BaseSettings):
            _register_environ(value)
        else:
            os.environ[field_name.upper()] = str(value)

            
@exception_handler
@lru_cache(maxsize=1)
def get_settings(into_env: bool = False) -> BaseSettings:
    try:
        settings = Settings()
    except Exception as e:
        raise ConfigLoadError("Settingsのインタスタンス化に失敗。", context={"error": str(e)})
    
    if into_env:
        _register_environ(settings)
    return settings