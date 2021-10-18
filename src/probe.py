import os
from pathlib import Path
from posixpath import splitext
from src.dataclass import variables as v
from src.dataclass import colors as c
from src.dataclass import statistics as stats


class Probe:
    def __init__(self) -> None:
        self.extenions = [".mp4", ".mkv"]
    def _info(self)->None:
        print(f"{c.BLUE}{c.BOLD}{'='*c.width}")
        print(f"{c.BLUE}Starting Probe{c.RESET}".center(c.width))
        print(f"{c.BLUE}{c.BOLD}{'='*c.width}")

    def _transverse_folder(self) -> None:
        for root, sub, files in os.walk(v.input_file_path):
            if files:
                for file in files:
                    file_name = splitext(file)[0]
                    file_extension = splitext(file)[1]
                    if file_extension in self.extenions:
                        file_path = Path(os.path.join(root, file)).absolute()
                        stats.total_files+=1
                        self._probe(file_path, file_name)
                    else:
                        print(f"{c.RED}{c.BOLD}{file} is not video file.{c.RESET}")
                        stats.total_files+=1


    def _probe(self, file_path: str, file_name: str) -> None:
        stats.total_probed_files+=1

    def run(self) -> None:
        self._info()
        self._transverse_folder()
