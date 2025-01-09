import tkinter as tk
from services.timer_service import TimerService
from services.lock_screen_service import LockScreenService

class PomodoroApp:
    def __init__(self, root, timer_service, lock_service):
        self.root = root
        self.timer_service = timer_service
        self.lock_service = lock_service

        self.time_var = tk.StringVar()
        self.time_var.set(self.format_time(self.timer_service.remaining_time))

        self.setup_ui()
        self.update_time()

    def setup_ui(self):
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x200")

        self.label = tk.Label(self.root, textvariable=self.time_var, font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def update_time(self):
        self.root.after(1000, self.update_time)
        if self.timer_service.running:
            self.timer_service.tick()
            self.time_var.set(self.format_time(self.timer_service.remaining_time))

            if self.timer_service.is_time_up():
                self.timer_service.reset()
                self.lock_service.lock_screen()

    def start_timer(self):
        self.timer_service.start()

    def pause_timer(self):
        self.timer_service.pause()

    def reset_timer(self):
        self.timer_service.reset()
        self.time_var.set(self.format_time(self.timer_service.remaining_time))

    @staticmethod
    def format_time(seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02}:{seconds:02}"
