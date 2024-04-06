import time
import pyautogui as pg
i = 1
while i == 1:
    print("start")
    time.sleep(3)
    pg.click(x = 177,y = 245, clicks = 2)
    time.sleep(3)
    pg.click(x = 160,y = 60)
    time.sleep(1)
    pg.write("www.baidu.com")
    time.sleep(2)
    pg.press('enter')
    time.sleep(1)
    pg.press('enter')
    break