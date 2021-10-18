import os
import sys
from pathlib import Path
from time import sleep

from src.dataclass import colors as c
from src.dataclass import variables as v
from src.probe import Probe


class main:
    def __init__(self) -> None:
        pass

    def _cls(self):
        os.system("cls" if os.name == "nt" else "clear")

    def _info(self) -> None:
        print(f"{c.GREEN}{c.BOLD}{'='*c.width}{c.RESET}")
        print(f"{c.ORANGE}{c.BOLD}FFMPEG Recursive Encoder{c.RESET}".center(c.width))
        print(f"{c.GREEN}{c.BOLD}{'='*c.width}{c.RESET}")
        print(
            f"{c.CYAN}This tool is meant to mass convert video files to h.265 with aac audio.{c.RESET}"
        )
        print(
            f"{c.CYAN}It encodes the video track and all the individual audio tracks, while keeping other tracks such as images, subtitles, or attachments intact.{c.RESET}"
        )

    def _checks(self) -> None:
        print(f"{c.BLUE}{c.BOLD}{'='*c.width}{c.RESET}")
        if sys.version_info < (3, 10):
            print(
                f"{c.RED}{c.BOLD}You must use Python 3.10.x or greater, please update{c.RESET}"
            )
            sleep(5)
            sys.exit(1)
        if os.name != "nt":
            print(
                f"{c.ORANGE}{c.BOLD}Warning: This tool was meant for windows but it can also run on Linux.{c.RESET}"
            )
            choice = input(
                f"{c.ORANGE}To make it work on linux,  aphostrophes need to be removed from all directories and file names. This program can do it automatically. {c.CYAN}Proceed? [Y/N]{c.RESET}"
            )
            if choice.lower() == "y":
                v.rename = True
            elif choice.lower() == "n":
                v.rename = False
            else:
                print(f"{c.RED}Invalid input. Defaulted to no.{c.RESET}")
                v.rename = False
        print(
            f"{c.CYAN}This tool supports hardware encoding, although ffmpeg needs to be configured with '--enable-nvenc' and a compatible gpu is required. If you meet these requirements you can enable hardware encoding on this tool.{c.RESET}"
        )
        choice = input(f"{c.ORANGE}Enable hardware encoding? [Y/N]{c.RESET}")
        if choice.lower() == "y":
            print(f"{c.GREEN}Enabled hardware encoding.{c.RESET}")
            v.hwacc = True
        elif choice.lower() == "n":
            print(f"{c.RED}Disabled hardware encoding.{c.RESET}")
            v.hwacc = False
        else:
            print(f"{c.RED}Invalid input. Defaulted to no.{c.RESET}")
            v.hwacc = False

        print(f"{c.BLUE}{c.BOLD}{'='*c.width}{c.RESET}")

    def _input(self) -> None:
        check=True
        while check:
            ipath = input(f"{c.CYAN}Enter input folder: {c.RESET}")
            if  os.path.isdir(ipath):
                check=False
            else:
                print(f"{c.RED}{c.BOLD}File path is not valid.{c.RESET}")
        check2=True
        while check2:
            opath = input(f"{c.CYAN}Enter output folder: {c.RESET}")
            if  os.path.isdir(opath):
                check2=False
            else:
                print(f"{c.RED}{c.BOLD}File path is not valid.{c.RESET}")
        
        
        v.input_file_path = Path(ipath).absolute()
        v.output_file_path = Path(opath).absolute()

    def run(self):
        self._cls()
        self._info()
        sleep(5)
        self._checks()
        self._input()


if __name__ == "__main__":
    main().run()
    Probe().run()
