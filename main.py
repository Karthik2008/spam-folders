import pyautogui as pg
import time

x = 0

time.sleep(1)

while True:
    x += 1
    pg.typewrite('mkdir ' + str(x) + '\n')
