import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


from services.timer_service import TimerService


def test_timer_initial_state():
    timer = TimerService(duration_minutes=25)
    assert timer.remaining_time == 25 * 60
    assert not timer.running
    assert not timer.paused

def test_start_timer():
    timer = TimerService(duration_minutes=25)
    timer.start()
    assert timer.running
    assert not timer.paused

def test_pause_timer():
    timer = TimerService(duration_minutes=25)
    timer.start()
    timer.pause()
    assert not timer.running
    assert timer.paused

def test_reset_timer():
    timer = TimerService(duration_minutes=25)
    timer.start()
    timer.tick()  # Simula un tick
    timer.reset()
    assert timer.remaining_time == 25 * 60
    assert not timer.running
    assert not timer.paused

def test_timer_tick():
    timer = TimerService(duration_minutes=1)
    timer.start()
    timer.tick()
    assert timer.remaining_time == (1 * 60 - 1)

def test_timer_reaches_zero():
    timer = TimerService(duration_minutes=1)
    timer.start()
    for _ in range(60):
        timer.tick()
    assert timer.remaining_time == 0
    assert timer.is_time_up()
