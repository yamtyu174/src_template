import os
import yaml
import logging.config
from pathlib import Path

# def setup_logger(config_path="src/logger/logging.yaml", name="app"):
#     config_text = Path(config_path).read_text(encoding="utf-8")
#     config_text = os.path.expandvars(config_text)
#     config = yaml.safe_load(config_text)
#     logging.config.dictConfig(config)
#     logger = logging.getLogger(name)
#     logger.info("✅ Logger initialized with environment integration.")
#     return logger

def _read_config_text() -> str:
    yaml_name = os.getenv("LOG_YAML", "basic.yaml")
    config_path = Path(__file__).parent / "logging_config" / yaml_name
    if not config_path.exists():
        raise FileNotFoundError(f"Logging config not found: {config_path}")
    config_text = Path(config_path).read_text(encoding="utf-8")
    return config_text

def setup_logger(name="app") -> logging.Logger:
    config_text = _read_config_text()
    config_text = os.path.expandvars(config_text)
    config = yaml.safe_load(config_text)
    logging.config.dictConfig(config)
    logger = logging.getLogger(name)
    logger.info("✅ Logger initialized with environment integration.")
    return logger
