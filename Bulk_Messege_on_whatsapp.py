import webbrowser
import time
import pyautogui as gui

interval = 1
position2 = 1875,978
position = 933,500
numbers = {9999988888, 1234567890, 9876543210 , 4584155451}

message="Hello, How Are you ??"

for i in numbers:
    url = 'https://wa.me/91{}?text={}'.format(i, message)
    webbrowser.open(url)
    time.sleep(3)
    gui.click(position)
    time.sleep(2)
    gui.click(position2)
    time.sleep(3)
    # gui.press('enter')
    time.sleep(interval)
    