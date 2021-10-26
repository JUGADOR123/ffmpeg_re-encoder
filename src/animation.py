import threading
import time
from dataclass import colors as c
from dataclass import statistics as t

frames = [
    f"{c.BLUE}{c.BOLD}[                 ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[=                ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[===              ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[====             ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[=====            ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[======           ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[=======          ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[========         ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[ ========        ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[  ========       ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[   ========      ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[    ========     ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[     ========    ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[      ========   ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[       ========  ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[        ======== ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[         ========]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[          =======]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[           ======]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[            =====]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[             ====]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[              ===]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[               ==]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[                =]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[                 ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[                =]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[               ==]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[              ===]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[             ====]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[            =====]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[           ======]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[          =======]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[         ========]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[       ========= ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[      =========  ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[     =========   ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[   =========     ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[  =========      ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[ =========       ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[=========        ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[========         ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[=======          ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[======           ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[=====            ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[====             ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[===              ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[==               ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[=                ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
    f"{c.BLUE}{c.BOLD}[                 ]{c.RESET}{c.GREEN} Encoding File... Time Remaining: {c.RED}{(t.time_remaining()/60)} Minutes{c.RESET}",
]
class Animation:
    def __init__(self) -> None:
        self.state:bool=True
        self.t=threading.Thread(target=self._animation)
    def _animation(self)->None:
            while self.state:
                for i in frames:
                    print(i, end="\r")
                    time.sleep(0.05)
    def run(self)->None:
        self.state=True
        self.t.start()
    def stop(self)->None:
        self.state=False
        self.t.join()




