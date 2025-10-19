import pytest
from settings import get_settings

@pytest.fixture(autouse=True)
def clear_cache():
    """全テスト前にSettingsキャッシュをクリア"""
    get_settings.cache_clear()
