import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import pytest
from unittest.mock import Mock, patch
from services.news_service import NewsService

@pytest.fixture
def mock_config_manager():
    """Simula un ConfigManager con valores de configuración."""
    mock_config = Mock()
    mock_config.get.side_effect = lambda *keys, **kwargs: {
        ("news_api", "base_url"): "http://mock-newsapi.org/v2/top-headlines",
        ("news_api", "api_key"): "mock_api_key"
    }.get(keys, kwargs.get("default"))
    return mock_config

@patch("services.news_service.requests.get")
def test_get_trending_news_success(mock_get, mock_config_manager):
    # Simular una respuesta exitosa de la API
    mock_get.return_value.json.return_value = {
        "articles": [{"title": f"News {i}"} for i in range(10)]
    }
    mock_get.return_value.status_code = 200

    service = NewsService(mock_config_manager)
    news = service.get_trending_news()

    assert len(news) == 10
    assert news[0] == "News 0"
