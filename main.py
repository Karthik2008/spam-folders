import pyautogui as pg
import time

x = 0

ask = int(input('how many times do you want to spam: '))

time.sleep(1)

for i in range(ask + 1):
    pg.typewrite('mkdir ' + str(x) + '\n')
    x += 1

time.sleep(1)

for i in range(ask + 2):
    pg.typewrite('rm -d ' + str(x) + '\n')
    x -= 1
