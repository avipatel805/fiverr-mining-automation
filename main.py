import pyautogui as pg
import time


def press(key, duration=0.1):
    with pg.hold(key):
        time.sleep(duration)


def spider(count):
    press('x')
    time.sleep(0.01)
    press('x')
    for _ in range(6):
        pg.press('right')
        time.sleep(0.08)

    spider_loc = None
    for _ in range(100):
        try:
            spider_loc = pg.locateOnScreen('spider.jpg', confidence=0.7)
            time.sleep(0.01)
        except pg.ImageNotFoundException:
            time.sleep(0.01)
            continue
    if spider_loc is not None:
        for _ in range(6):
            pg.press('right')
            time.sleep(0.08)
        press('z')
        time.sleep(0.01)
        press('z')


def mine_collapse():
    press('down', 3)
    time.sleep(0.07)
    press('up', 0.5)
    with pg.hold('up') and pg.hold('left'):
        time.sleep(0.7)


def mine():
    for _ in range(4):
        pg.press('left')
        time.sleep(0.300)
    time.sleep(0.6)

    spider_loc = None
    for _ in range(100):
        try:
            spider_loc = pg.locateOnScreen('spider.jpg', confidence=0.7)
            time.sleep(0.01)
        except pg.ImageNotFoundException:
            time.sleep(0.01)
            continue
    if spider_loc is not None:
        spider()

    mine_loc = None
    for _ in range(100):
        try:
            mine_loc = pg.locateOnScreen('fire.png', confidence=0.7)
            time.sleep(0.01)
        except pg.ImageNotFoundException:
            time.sleep(0.01)
            continue

    if mine_loc is not None:
        mine_collapse()
        return False

    press('up', 0.07)
    return True


def main():
    counter = 0
    while counter < 15:
        if mine():
            counter += 1
        else:
            counter = 0
    press('down', 2.5)
    main()


if __name__ == "__main__":
    main()
