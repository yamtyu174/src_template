from typing import Optional
from dataclasses import dataclass

@dataclass
class BaseAppException(Exception):
    """アプリケーション全体の基底例外"""
    message: str
    context: Optional[dict] = None

    def __str__(self) -> str:
        base = f"[{self.__class__.__name__}] {self.message}"
        if self.context:
            return f"{base} | context={self.context}"
        return base
