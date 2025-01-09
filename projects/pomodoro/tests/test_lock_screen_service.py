import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from unittest.mock import patch
from services.lock_screen_service import LockScreenService


@patch("services.lock_screen_service.ctypes.windll.user32.LockWorkStation")
def test_lock_screen_windows(mock_lock):
    LockScreenService.lock_screen()
    if os.name == "nt":  # Solo se ejecuta en Windows
        mock_lock.assert_called_once()

@patch("services.lock_screen_service.os.system")
def test_lock_screen_linux_mac(mock_system):
    LockScreenService.lock_screen()
    if os.name == "posix":  # Solo se ejecuta en Linux/macOS
        mock_system.assert_called_once()
