import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import pytest
from unittest.mock import Mock, patch
from services.horoscope_service import HoroscopeService

@pytest.fixture
def mock_config_manager():
    """Simula un ConfigManager con valores de configuración."""
    mock_config = Mock()
    mock_config.get.side_effect = lambda *keys, **kwargs: {
        ("horoscope", "base_url"): "http://mock-horoscope.com"
    }.get(keys, kwargs.get("default"))
    return mock_config

@patch("services.horoscope_service.requests.get")
def test_get_horoscope_success(mock_get, mock_config_manager):
    # Simular una respuesta HTML válida con un único elemento
    mock_get.return_value.text = """
        <html>
        <body>
            <h1>Aries Horoscope</h1>
            <div class="main-horoscope">
                <p>Today will be a great day!</p>
            </div>
        </body>
        </html>
    """

    service = HoroscopeService(mock_config_manager)
    horoscope = service.get_horoscope("aries")

    assert "Today will be a great day!" in horoscope

