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
    ) -> None:
        self.folder = Path(folder) if isinstance(folder, str) else folder
        self.vcodecs: List[str] = None
        self.acodecs: List[str] = None
        self.containers: List[str] = None
        self.valid_video_extensions: List[str] = [".mkv", ".mp4"]
        self._failed_files = []