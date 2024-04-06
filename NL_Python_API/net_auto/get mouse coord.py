import os,time
import pyautogui as pg
try:
    while True:
        print("crtl + c return")
        x , y = pg.position()
        poststr = "Now mouse position:" + str(x).rjust(4) + "," + str (y).rjust(4)
        print(poststr)
        time.sleep(2)
        # system commend to clean screen
        os.system("cls")
except KeyboardInterrupt:
    # keyyboard... a commend to make mistake.(crtl + c)
    print("returned")

