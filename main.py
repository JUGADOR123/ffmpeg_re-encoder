import json
import time
import os
import shlex
import subprocess
from posixpath import splitext
from typing import List, Literal, Union


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
        self.folder = folder
        self.vcodecs = vcodecs
        self.acodecs = acodecs
        self.containers = containers
        self.valid_video_extensions = valid_video_extensions
        self._failed_files = failed_files
        self.blacklist = blacklist

    def analysis(self) -> None:
        """Checks for incompatible folder names"""
        newdir = []
        for root, sub, file in os.walk(self.folder, topdown=False):
            if self.blacklist in root:
                nd = root.replace(self.blacklist, " ")
                print(f"New Directory: {nd}")

                os.rename(root, nd)
            else:
                pass
                # print(f"No change required: {root}")


# folder = input("Enter Absolute folder path: ")
folder = r"C:\Users\Jugador\Desktop\test"
program(folder).analysis()
