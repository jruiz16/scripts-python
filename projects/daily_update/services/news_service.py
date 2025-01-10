import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../venv/lib/site-packages")))

import requests

class NewsService:
    def __init__(self, config_manager):
        self.base_url = config_manager.get("news_api", "base_url")
        self.api_key = config_manager.get("news_api", "api_key")
        self.sources = config_manager.get("news_api", "sources")

    def get_trending_news(self):
        """Fetch and return trending news headlines."""
        url = f"{self.base_url}?sources={self.sources}&apiKey={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            articles = response.json()["articles"]
            return [ar["title"] for ar in articles[:10]]
        except Exception as e:
            return [f"Error fetching news: {e}"]
