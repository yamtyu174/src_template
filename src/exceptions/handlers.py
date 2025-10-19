from functools import wraps
import logging
from .base import BaseAppException

logger = logging.getLogger(__name__)

# デコレーターで使用。
# 外がわでキャッチする
def exception_handler(func) -> None | object:
    """関数レベルの例外ハンドラ"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseAppException as e:
            logger.error(str(e))
            raise
        except Exception as e:
            logger.critical(f"Unexpected error: {e}", exc_info=True)
            raise
    return wrapper
