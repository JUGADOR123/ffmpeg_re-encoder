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
        base_path: str = None,
        vcodecs: List[str] = None,
        acodecs: List[str] = None,
        containers: List[str] = None,
        valid_video_extensions: List[str] = [".mkv", ".mp4"],
        blacklist: str = "'",
        failed_files: List[str] = None,
    ) -> None:
        self.base_path = base_path
        self.vcodecs = vcodecs
        self.acodecs = acodecs
        self.containers = containers
        self.valid_video_extensions = valid_video_extensions
        self._failed_files = failed_files
        self.blacklist = blacklist

    def analysis(self) -> None:
        """Checks for incompatible base_path names"""
        subdirectories=[]

            




# base_path = input("Enter Absolute folder path: ")
base_path = r"C:\Users\Jugador\Desktop\test"
program(base_path).analysis()

