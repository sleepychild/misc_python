import signal
import pyautogui

from time import sleep
from typing import List, Tuple

IMG_PATH: str = "infinite_cosmos/img/"

BREAKTHROUGH_IMAGE_PATH: str = IMG_PATH + "breakthrough.png"
UPGRADE_IMAGE_PATH: str = IMG_PATH + "upgrade.png"
UPDATE_IMAGE_PATH: str = IMG_PATH + "update.png"
HOLO_BLUE_A_IMAGE_PATH: str = IMG_PATH + "holo_blue_a.png"
HOLO_BLUE_B_IMAGE_PATH: str = IMG_PATH + "holo_blue_b.png"


class GameAutomator:
    class UpgTrgt:
        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y

        def click(self) -> None:
            pyautogui.click(self.x, self.y)

    def __init__(self) -> None:
        # Handle KeyboardInterupt
        self.running: bool = True
        signal.signal(signal.SIGINT, self._sigint_handler)

        # Create game screen rect
        _: str = input("Place mouse at top left end of game screen")
        self.left, self.top = pyautogui.position()

        _: str = input("Place mouse at bottom right end of game screen")
        self.right, self.bottom = pyautogui.position()

        self.width: int = self.right - self.left
        self.height: int = self.bottom - self.top

        self.game_rect: Tuple[int] = (self.left, self.top, self.width, self.height)

        # self.upgrades: List[self.UpgTrgt] = list()
        self.set_upgrades()

    def set_upgrades(self) -> None:
        self.upgrades: List[self.UpgTrgt] = [
            self.UpgTrgt(*pyautogui.center(ut))
            for ut in pyautogui.locateAllOnScreen(
                UPGRADE_IMAGE_PATH,
                grayscale=False,
                confidence=0.9,
                region=self.game_rect,
            )
        ]

    def breakthrough(self) -> None:
        breakthrough = pyautogui.locateCenterOnScreen(
            BREAKTHROUGH_IMAGE_PATH,
            grayscale=False,
            confidence=0.6,
            region=self.game_rect,
        )
        print(f"BREAKTHROUGH: {breakthrough}")
        if not breakthrough == None:
            pyautogui.click(*breakthrough, clicks=400, interval=0.05)

    def upgrade(self) -> None:
        for up in self.upgrades:
            print(f"UPGRADE CLICK AT X: {up.x} Y: {up.y}")
            up.click()

    def holo_blue(self) -> None:
        holo_blue_a = pyautogui.locateCenterOnScreen(
            HOLO_BLUE_A_IMAGE_PATH,
            grayscale=False,
            confidence=0.4,
            region=self.game_rect,
        )
        holo_blue_b = pyautogui.locateCenterOnScreen(
            HOLO_BLUE_B_IMAGE_PATH,
            grayscale=False,
            confidence=0.4,
            region=self.game_rect,
        )
        print(f"HOLO A: {holo_blue_a} HOLO B: {holo_blue_b}")
        if not holo_blue_a == None:
            pyautogui.click(*holo_blue_a)
        if not holo_blue_b == None:
            pyautogui.click(*holo_blue_b)

    def play(self) -> None:
        while self.running:
            init_x, init_y = pyautogui.position()

            self.holo_blue()
            self.breakthrough()
            self.upgrade()

            pyautogui.moveTo(self.top, self.left)
            sleep(1)
            pyautogui.moveTo(init_x, init_y)
            sleep(5)

    def _sigint_handler(self, signal, frame) -> None:
        print(f" SIGNAL: {signal} FRAME: {frame}")
        self.running = False


if __name__ == "__main__":
    ga: GameAutomator = GameAutomator()
    ga.play()
