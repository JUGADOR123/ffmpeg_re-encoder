import subprocess
from time import sleep
from src.dataclass import variables as v
from src.dataclass import statistics as stats
from src.dataclass import errors as err
from src.dataclass import colors as c
class Encoder:
    def __init__(self) -> None:
        pass
    def _iterate(self) -> None:
        if v.video_tracks_to_encode:
            for path in v.video_tracks_to_encode:
                self._encoding(path)
    def _encoding(self,path:str) -> None:
        try:
            p=subprocess.Popen(f'ffmpeg -v quiet -i "{path}" -map 0 -c copy -c:v hevc_nvenc -preset p7 -rc cbr')
        except Exception as e:
            pass

    def _info(self)-> None:
        print(f"{c.RED}{c.BOLD}{'='*c.width}{c.RESET}")
        print(f"{c.GREEN}{c.BOLD}Encoding will start now{c.RESET}")
        print(f"{c.RED}{c.BOLD}{'='*c.width}{c.RESET}")
    def run(self) -> None:
        self._info()
        sleep(5)
        self._iterate()