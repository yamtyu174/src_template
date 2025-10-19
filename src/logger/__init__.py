import os
from .setup import setup_logger

from settings import get_settings

class LoggingEnvironmentError(Exception):
    pass

def _check_environ(env_name):
    if env_name not in os.environ:
        get_settings(into_env=True)
        if env_name not in os.environ:
            raise LoggingEnvironmentError(f"{env_name}を環境変数にセットしてください。")

requirement_environment = ["LOG_DIR", "LOG_LEVEL"]

for env_name in requirement_environment:
    _check_environ(env_name)

__all__ =  [
    "setup_logger"
]