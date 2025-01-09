from tkinter import Tk
from services.timer_service import TimerService
from services.lock_screen_service import LockScreenService
from ui.app_ui import PomodoroApp

if __name__ == "__main__":
    root = Tk()
    timer_service = TimerService(duration_minutes=25)
    lock_service = LockScreenService()
    app = PomodoroApp(root, timer_service, lock_service)
    root.mainloop()
