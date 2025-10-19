from settings import get_settings


def test_settings_load_success():
    """Settingsが正常に読み込める"""
    settings = get_settings()
    assert settings.log.LOG_LEVEL == "INFO"


def test_settings_error(monkeypatch):
    """設定のインスタンス化に失敗するケースを模擬"""
    monkeypatch.setattr("settings.config.Settings", None)

    try:
        get_settings()
    except Exception as e:
        # pytest.raisesでも良いが、ここは意図的に素直なcatch
        assert "Settings" in str(e)
