from time import sleep
from loginHeroku import HerokuAdmin
import pyautogui

def found_screen(fileName):
    return (pyautogui.locateCenterOnScreen(fileName) is not None)

def test_loginHeroku():
    herokuAdmin = HerokuAdmin()

    sleep(5)
    assert found_screen('success_icon.png')