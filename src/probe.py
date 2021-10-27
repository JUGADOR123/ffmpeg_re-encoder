import json
import os
from pathlib import Path
from posixpath import splitext
import subprocess
from src.dataclass import variables as v
from src.dataclass import colors as c
from src.dataclass import statistics as stats
from time import sleep

from src.statistics import Statistics


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
        print(f"{c.BLUE}{c.BOLD}{'Probing:':15s}{c.GREEN}{file_name}{c.RESET}")
        command1 = f'ffprobe -v quiet -of json -select_streams v:0 -show_entries stream=codec_name "{file_path}"'
        command2 = f'ffprobe -v quiet -of json -select_streams a:0 -show_entries stream=codec_name "{file_path}"'
        print(f"{c.ORANGE}{c.BOLD}{'File Size:':15s}{c.CYAN}{(round(os.path.getsize(file_path)/(1024*1024)))} MB{c.RESET}")
        try:
            output=subprocess.check_output(command1).decode("utf-8")
            data=json.loads(output)
            print(f"{c.ORANGE}{c.BOLD}{'Video Codec: ':15s}{c.CYAN}{data['streams'][0]['codec_name']}{c.RESET}")
            output=subprocess.check_output(command2).decode("utf-8")
            data=json.loads(output)
            print(f"{c.ORANGE}{c.BOLD}{'Audio Codec: ':15s}{c.CYAN}{data['streams'][0]['codec_name']}{c.RESET}")
        except subprocess.CalledProcessError as e:
            print(f"{c.RED}{c.BOLD}{e.output}{c.RESET}")
            stats.total_failed_probed_files+=1
        stats.total_probed_files+=1

    def run(self) -> None:
        self._info()
        sleep(5)
        self._transverse_folder()
        Statistics().probe_statistics()
