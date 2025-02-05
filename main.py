import pyautogui as pg
import time


def spider(count):
    pg.typewrite('x')
    time.sleep(0.01)
    pg.typewrite('x')
    for _ in range(6):
        pg.press('right')
        time.sleep(0.08)

    spider_loc = None
    for _ in range(100):
        spider_loc = pg.locateOnScreen('spider.jpg', confidence=0.7)
        time.sleep(0.01)
    if spider_loc is not None:
        for _ in range(6):
            pg.press('right')
            time.sleep(0.08)
        pg.typewrite('z')
        time.sleep(0.01)
        pg.typewrite('z')


def mine_collapse():
    with pg.hold('down'):
        time.sleep(3)
    time.sleep(0.07)
    with pg.hold('up'):
        time.sleep(0.5)
    with pg.hold('up') and pg.hold('left'):
        time.sleep(0.7)


def mine():
    for _ in range(4):
        pg.press('left')
        time.sleep(0.300)
    time.sleep(0.6)

    spider_loc = None
    for _ in range(100):
        spider_loc = pg.locateOnScreen('spider.jpg', confidence=0.7)
        time.sleep(0.01)
    if spider_loc is not None:
        spider()

    mine_loc = None
    for _ in range(100):
        mine_loc = pg.locateOnScreen('fire.png', confidence=0.7)
        time.sleep(0.01)

    if mine_loc is not None:
        mine_collapse()
        return False

    with pg.hold('up'):
        time.sleep(0.07)
    return True


def main():
    counter = 0
    while counter < 15:
        if mine():
            counter += 1
        else:
            counter = 0
    with pg.hold('down'):
        time.sleep(2.5)
    main()


if __name__ == "__main__":
    main()
