import tkinter as tk
from tkinter import ttk
from datetime import datetime

class DailyUpdateApp:
    def __init__(self, root, news_service, horoscope_service, history_service):
        self.root = root
        self.news_service = news_service
        self.horoscope_service = horoscope_service
        self.history_service = history_service
        self.setup_ui()

    def setup_ui(self):
        self.root.title(f"Daily Update: {datetime.now().strftime('%d %b %Y')}")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f5")

        # Canvas and scrollbar
        canvas = tk.Canvas(self.root, bg="#f0f0f5")
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f0f5")

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Sections
        self.create_section(scrollable_frame, "Trending News", "\n".join(self.news_service.get_trending_news()))
        self.create_section(scrollable_frame, "Horoscope", self.horoscope_service.get_horoscope("aries"))
        self.create_section(scrollable_frame, "On This Day", "\n".join(self.history_service.get_history_today()))

        # Close button
        close_button = ttk.Button(scrollable_frame, text="Close", command=self.root.destroy)
        close_button.pack(pady=20)

    def create_section(self, parent, title, content):
        frame = tk.Frame(parent, bg="#ffffff", pady=10, padx=10)
        frame.pack(fill="x", pady=5, padx=5)
        title_label = tk.Label(frame, text=title, font=("Arial", 14, "bold"), bg="#ffffff")
        title_label.pack(anchor="w", pady=(0, 5))
        content_label = tk.Label(frame, text=content, wraplength=450, justify="left", bg="#ffffff")
        content_label.pack(anchor="w")
