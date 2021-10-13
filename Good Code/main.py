import shutil
import time
#from src.renaming import Rename
from src.probe import Probe
import math
import src.variables
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
str_time=time.time()

def checks():
    print(sys.version)    

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
    time.sleep(5)
    Probe(indir, outdir).run()
def out():
    print(f'{CYAN}{BOLD}{"=" * width}{RESET}')
    print(f"{CYAN}Total time ellapsed: {(math.trunc(time.time()-str_time))/60} Minutes")
    print(f"{CYAN}Average ellapsed time: {((math.trunc(time.time()-str_time))/60)/src.variables.total_files} Minutes/file{RESET}")
    print(f"{CYAN}Total Files: {src.variables.total_files}{RESET}")
    print(f"{CYAN}Total encoded files: {src.variables.total_encoded_files}{RESET}")
    print(f"{CYAN}Total pre encoding size: {round(src.variables.total_pre_encoding_size,3)} GB {RESET}")
    print(f"{CYAN}Total post encoding size: {round(src.variables.total_post_encoding_size,3)} GB {RESET}")
    print(f"{CYAN}Space Saved: {round((src.variables.total_pre_encoding_size-src.variables.total_post_encoding_size),3)} GB{RESET}")
    print(f'{CYAN}{BOLD}{"=" * width}{RESET}')


indir = input("Enter input folder path: ")
outdir = input("Enter output folder path: ")
#path = r"C:\Users\Jugador\Desktop\test"

if __name__ == "__main__":
    checks()
    #src.variables.init()
    #main()
    #out()
