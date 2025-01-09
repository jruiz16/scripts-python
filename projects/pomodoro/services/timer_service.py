class TimerService:
    def __init__(self, duration_minutes):
        self.duration = duration_minutes * 60
        self.remaining_time = self.duration
        self.running = False
        self.paused = False

    def start(self):
        if not self.running:
            self.running = True
            self.paused = False

    def pause(self):
        if self.running:
            self.running = False
            self.paused = True

    def reset(self):
        self.running = False
        self.paused = False
        self.remaining_time = self.duration

    def tick(self):
        if self.running and self.remaining_time > 0:
            self.remaining_time -= 1
        return self.remaining_time

    def is_time_up(self):
        return self.remaining_time == 0
