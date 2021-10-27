import threading
import time
from dataclass import colors as c
from dataclass import statistics as t


class Animation:
    def __init__(self) -> None:
        self.state: bool = True
        self.t = threading.Thread(target=self._animation)
        self.time_remaining = t.time_remaining()
        self.frames = [
            f"{c.BLUE}{c.BOLD}[                 ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[=                ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[===              ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[====             ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[=====            ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[======           ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[=======          ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[========         ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[ ========        ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[  ========       ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[   ========      ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[    ========     ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[     ========    ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[      ========   ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[       ========  ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[        ======== ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[         ========]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[          =======]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[           ======]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[            =====]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[             ====]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[              ===]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[               ==]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[                =]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[                 ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[                =]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[               ==]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[              ===]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[             ====]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[            =====]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[           ======]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[          =======]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[         ========]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[       ========= ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[      =========  ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[     =========   ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[   =========     ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[  =========      ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[ =========       ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[=========        ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[========         ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[=======          ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[======           ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[=====            ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[====             ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[===              ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[==               ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[=                ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
            f"{c.BLUE}{c.BOLD}[                 ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(self.time_remaining/60)} Minutes{c.RESET}",
        ]

    def _animation(self) -> None:
        while self.state:
            for i in self.frames:
                print(i, end="\r")
                time.sleep(0.05)

    def run(self) -> None:
        self.state = True
        self.t.start()

    def stop(self) -> None:
        self.state = False
        self.t.join()
