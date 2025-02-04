import pyautogui as pg
import time


def spider():
    pass


def mine_collapse():
    pass


def mine():
    for _ in range(4):
        pg.press('left')
        time.sleep(0.300)
    time.sleep(0.6)

    spider_loc = None
    for _ in range(300):
        spider_loc = pg.locateOnScreen('spider.png', confidence=0.7)
        time.sleep(0.01)
    if spider_loc is not None:
        spider()

    mine_loc = None
    for _ in range(300):
        mine_loc = pg.locateOnScreen('fire.png', confidence=0.7)
        time.sleep(0.01)

    if mine_loc is not None:
        mine_collapse()

    with pg.hold('up'):
        time.sleep(0.07)


def main():
    pass


if __name__ == "__main__":
    main()

