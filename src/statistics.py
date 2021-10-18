from src.dataclass import colors as c
from src.dataclass import variables as v
from src.dataclass import statistics as stat
from time import time

class Statistics:
    def __init__(self) -> None:
        pass
    def _print(self)->None:
        #print(f"{c.GREEN}{c.RESET}")
        print(f"{c.ORANGE}{c.BOLD}{'='*c.width}{c.RESET}")
        print(f"{c.GREEN}Time taken: {(stat.starting_time-stat.ending_time)/60}{c.RESET}")
        print(f"{c.GREEN}Total files found: {stat.total_files}{c.RESET}")
        print(f"{c.GREEN}Total renamed files: {stat.total_files_renamed}{c.RESET}")
        print(f"{c.GREEN}Total files probed: {stat.total_probed_files}{c.RESET}")
        print(f"{c.GREEN}Total number of encoded files: {stat.total_number_of_encoded_files}{c.RESET}")
        print(f"{c.ORANGE}{c.BOLD}{'='*c.width}{c.RESET}")
    def run(self)-> None:
        stat.ending_time=time()
        self._print()