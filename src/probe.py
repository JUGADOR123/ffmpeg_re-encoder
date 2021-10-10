from pathlib import Path
from posixpath import splitext
from time import sleep
from typing import List
from src.reencode import Encode
import os
import shutil
import json
import subprocess
import math

HEADER = "\033[95m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
ORANGE = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"
width = shutil.get_terminal_size((80, 20)).columns


class Probe:
    def __init__(self, base_folder: Path, output_dir: Path) -> None:
        self.base_folder = Path(base_folder).absolute()
        self.output_dir = Path(output_dir).absolute()
        self.items: List[str] = []
        self.failed_items: List[str] = []
        self.keys: List[str] = []
        self.acodecs = []
        self.vcodecs = []
        self.extenions = [".mp4", ".mkv"]

    def _recursive_dict(self, subdict: dict) -> None:
        if subdict["codec_type"] == "video":

            if subdict['codec_name'] not in self.vcodecs:
                self.vcodecs.append(subdict['codec_name'])

            print(
                f"{GREEN}Video Codec: {ORANGE}{subdict['codec_name']}{RESET}")
        elif subdict["codec_type"] == "audio":

            if subdict['codec_name'] not in self.acodecs:
                self.acodecs.append(subdict['codec_name'])
            print(
                f"{GREEN}Audio Codec: {ORANGE}{subdict['codec_name']}{RESET}")
        elif subdict["codec_type"] == "subtitle":
            f"{GREEN}Subtitle Codec: {ORANGE}{subdict['codec_name']}{RESET}"
        elif subdict["codec_type"] == "attachment":
            f"{GREEN}Subtitle Codec: {ORANGE}{subdict['codec_name']}{RESET}"
        else:
            print(f"{RED}{BOLD}Unknown Track{RESET}")
            print(f"{RED}{BOLD}Codec type: {subdict['codec_type']}{RESET}")
            print(f"{RED}{BOLD}Codec Name: {subdict['codec_name']}{RESET}")
            print(
                f"{RED}{BOLD}Codec Long Name:{subdict['codec_long_name']}{RESET}"
            )
            sleep(5)
        for key in subdict.keys():
            if key not in self.keys:
                self.keys.append(key)

    def _probe(self, file: Path, file_name) -> None:
        command = f'ffprobe -v quiet -print_format json -show_streams "{file}"'
        print(f'{ORANGE}{"=" * width}{RESET}')
        print(f"{ORANGE}Inspecting:  {file_name}{RESET}")
        size=os.path.getsize(file)
        print(f"{BLUE}{BOLD}File Size: {math.trunc((size/(1024*1024)))} MB")
        try:
            output = subprocess.check_output(command).decode("utf-8")
            data = json.loads(output)
            for subdict in data["streams"]:
                self._recursive_dict(subdict)
        except Exception as e:
            print(f"{RED}{BOLD}ERROR INSPECTING FILE: {e}{RESET}")
            self.failed_items.append((file_name, e))
            print(f'{ORANGE}{"=" * width}{RESET}')
        else:
            self.items.append(file_name)
            if len(self.acodecs) != 0 and len(self.vcodecs) != 0:
                Encode(file, self.output_dir, self.acodecs, self.vcodecs).run()
                self.acodecs.clear()
                self.vcodecs.clear()
                print(f'{ORANGE}{"=" * width}{RESET}')
            sleep(1)

    def run(self) -> None:
        for root, sub, files in os.walk(self.base_folder):
            if files:
                for file in files:
                    file_name = splitext(file)[0]
                    file_extension = splitext(file)[1]
                    if file_extension in self.extenions:
                        file_path = Path(os.path.join(root, file))
                        self._probe(file_path, file_name)
                    else:
                        print(
                            f"{RED}{BOLD}{file_name}{file_extension}: Not a video file{RESET}"
                        )
                        sleep(1)
