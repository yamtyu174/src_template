from .base import BaseAppException

class ConfigLoadError(BaseAppException):
    """設定ファイルの読み込み失敗"""

class LogInitializationError(BaseAppException):
    """ロガー初期化失敗"""

class LoggingEnvironmentError(BaseAppException):
    """ロガーに必要な環境変数の欠如"""