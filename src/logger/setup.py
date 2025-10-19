import os
import yaml
import logging.config
from pathlib import Path
from functools import lru_cache

from exceptions import exception_handler, LogInitializationError, LoggingEnvironmentError

def _check_environ(env_name):
    if env_name not in os.environ:
        raise LoggingEnvironmentError(f"{env_name}を環境変数にセットしてください。")

def _read_config_text() -> str:
    yaml_name = os.getenv("LOG_YAML", "basic.yaml")
    config_path = Path(__file__).parent / "logging_config" / yaml_name
    if not config_path.exists():
        raise FileNotFoundError(f"Logging config not found: {config_path}")
    config_text = Path(config_path).read_text(encoding="utf-8")
    return config_text


@lru_cache(maxsize=3)
def setup_logger(name="app") -> logging.Logger | None:
    requirement_environment = ["LOG_DIR", "LOG_LEVEL"]
    try:
        for env_name in requirement_environment:
            _check_environ(env_name)
        config_text = _read_config_text()
        config_text = os.path.expandvars(config_text)
        config = yaml.safe_load(config_text)
        logging.config.dictConfig(config)
        logger = logging.getLogger(name)
        logger.info("✅ Logger initialized with environment integration.")
        return logger
    except Exception as e:
        raise LogInitializationError("loggerのセットアップに失敗", context={"error": str(e)})