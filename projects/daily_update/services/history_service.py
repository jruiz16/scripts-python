import requests
from bs4 import BeautifulSoup

class HistoryService:
    def __init__(self, config_manager):
        self.base_url = config_manager.get("history", "base_url")

    def get_history_today(self):
        """Fetch and return historical events that happened on this day."""
        try:
            response = requests.get(self.base_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            history_list = soup.select('.event')[:5]
            return [event.getText().strip() for event in history_list]
        except Exception as e:
            return [f"Error fetching history: {e}"]
