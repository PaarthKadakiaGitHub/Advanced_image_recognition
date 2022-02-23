from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time
import keyboard
import win32api, win32con
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.agame.com/game/magic-piano-tiles")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

time.sleep(5)
click(760,720)
time.sleep(2)
click(360,570)
time.sleep(30)
click(450, 600)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(250, 400)[0] == 0:
        click(250, 400)
    if pyautogui.pixel(350, 400)[0] == 0:
        click(350, 400)
    if pyautogui.pixel(450, 400)[0] == 0:
        click(450, 400)
    if pyautogui.pixel(550, 400)[0] == 0:
        click(550, 400)