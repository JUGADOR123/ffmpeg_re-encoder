import json
import time
import os
import shlex
import subprocess
from posixpath import splitext
from typing import List, Literal, Union
from pathlib import Path


class program:
    def __init__(
        self,
        folder: str = None,
        vcodecs: List[str] = None,
        acodecs: List[str] = None,
        containers: List[str] = None,
        valid_video_extensions: List[str] = [".mkv", ".mp4"],
        blacklist: str = "'",
        failed_files: List[str] = None,
    ) -> None:
        self.folder = Path(folder) if isinstance(folder, str) else folder
        self.vcodecs = vcodecs
        self.acodecs = acodecs
        self.containers = containers
        self.valid_video_extensions = valid_video_extensions
        self._failed_files = failed_files
        self.blacklist = blacklist

    def analysis(self) -> None:
        """Checks for incompatible folder names"""
        self.process_folder(self.folder, self.blacklist, " ")

    def process_folder(self, current_folder: Path, to_replace: str, replacement: str):
        rename_folder = lambda folder, old, new: folder.rename(
            folder.parent / folder.name.replace(old, new)
        )  # this is just to make it more readable
        current_folder = rename_folder(
            current_folder, to_replace, replacement
        )  # check current folder
        for item in current_folder.iterdir():
            if item.is_dir() and self.blacklist in item.name:
                old_name = item.name
                item = rename_folder(item, to_replace, replacement)
                print(f"Renamed {old_name} to {item.name}")
                self.process_folder(item, to_replace, replacement)
            


# folder = input("Enter Absolute folder path: ")
path = r"C:\Users\Jugador\Desktop\test"
program(path).analysis()
