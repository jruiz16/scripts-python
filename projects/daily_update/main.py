import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import tkinter as tk
from utils.config_manager import ConfigManager
from projects.daily_update.services.news_service import NewsService
from projects.daily_update.services.horoscope_service import HoroscopeService
from projects.daily_update.services.history_service import HistoryService
from projects.daily_update.ui.app_ui import DailyUpdateApp

if __name__ == "__main__":
    config_path = os.path.dirname(__file__) + "/config/config.json"

    config_manager = ConfigManager(config_path=config_path)

    news_service = NewsService(config_manager)
    horoscope_service = HoroscopeService(config_manager)
    history_service = HistoryService(config_manager)

    root = tk.Tk()
    app = DailyUpdateApp(root, news_service, horoscope_service, history_service)
    root.mainloop()
