import shutil
from time import sleep
#from src.renaming import Rename
from src.probe import Probe
import sys

width = shutil.get_terminal_size((80, 20)).columns
HEADER = "\033[95m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
ORANGE = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"


def main():
    #print(f'{CYAN}{BOLD}{"=" * width}{RESET}')
    #print(f"{CYAN}Starting analysis on folders{RESET}")
    #print(f'{CYAN}{BOLD}{"=" * width}{RESET}')
    #sleep(5)
    #check=Rename(to_remove="'",to_add=" ",base_folder=path).run()
    #if check:
    #    print(f'{RED}{BOLD}{"=" * width}{RESET}')
    #    print(f"{RED}{BOLD}ERRORS FOUND: STOPPING EXECUTION{RESET}")
    #    print(f'{RED}{BOLD}{"=" * width}{RESET}')
    #    sys.exit(1)
    #print(f"{CYAN}{BOLD}NO ERRORS FOUND{RESET}")
    print(f'{ORANGE}{BOLD}{"=" * width}{RESET}')
    print(f"{ORANGE}{BOLD}Probing & Re-encoding files{RESET}".center(width))
    print(f'{ORANGE}{BOLD}{"=" * width}{RESET}')
    sleep(5)
    Probe(indir, outdir).run()


indir = input("Enter input folder path: ")
outdir = input("Enter output folder path: ")
#path = r"C:\Users\Jugador\Desktop\test"

if __name__ == "__main__":
    main()
