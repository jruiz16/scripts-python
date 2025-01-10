import requests
from bs4 import BeautifulSoup

class HoroscopeService:
    def __init__(self, config_manager):
        self.base_url = config_manager.get("horoscope", "base_url")

    def get_horoscope(self, sign_name):
        """Fetch and return horoscope for the specified sign."""
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        signs = {
            'aries': 1, 'taurus': 2, 'gemini': 3, 'cancer': 4,
            'leo': 5, 'virgo': 6, 'libra': 7, 'scorpio': 8,
            'sagittarius': 9, 'capricorn': 10, 'aquarius': 11, 'pisces': 12
        }

        sign_id = signs.get(sign_name.lower())
        if sign_id is None:
            return f"Error fetching horoscope: invalid sign '{sign_name}'"

        url = f"{self.base_url}?sign={sign_id}"
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            horoscope_text = soup.select('.main-horoscope p')[0].getText().strip().capitalize()
            return horoscope_text
        except Exception as e:
            return f"Error fetching horoscope: {e}"
