import logging
from logger import setup_logger


def test_logger_success(monkeypatch):
    """正常系: ロガーが正しく初期化される"""
    monkeypatch.setenv("LOG_DIR", "src/logger/logs")
    monkeypatch.setenv("LOG_LEVEL", "INFO")

    logger = setup_logger()
    assert isinstance(logger, logging.Logger)
    assert logger.name == "app"


def test_logger_missing_env(monkeypatch):
    """正常系: LOG_DIRが未設定の場合はデフォルト値"""
    monkeypatch.delenv("LOG_DIR", raising=False)
    monkeypatch.setenv("LOG_LEVEL", "INFO")

    logger = setup_logger()

    assert isinstance(logger, logging.Logger)
    assert logger.name == "app"
