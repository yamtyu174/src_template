import logging
from logger import setup_logger

def test_logger_initialization(monkeypatch):
    monkeypatch.setenv("LOG_DIR", "src/logger/logs")
    monkeypatch.setenv("LOG_LEVEL", "INFO")

    logger = setup_logger()
    assert isinstance(logger, logging.Logger)
    assert logger.name == "app"
