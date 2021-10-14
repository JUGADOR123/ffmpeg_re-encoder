from dataclasses import dataclass
from typing import List
from shutil import get_terminal_size


@dataclass
class statistics:
    """A class that holds all the statistic based variables"""

    total_files: int
    total_files_renamed: int
    total_failed_renamed_files: int
    total_probed_files: int
    total_failed_probed_files: int
    total_number_of_files_to_encode: int
    remaining_files_to_encode: int
    total_number_of_encoded_files: int
    total_number_of_failed_encodes: int
    starting_time: float
    ending_time: float
    individual_encoding_starting_time: float
    individual_encoding_ending_time: float
    initial_file_size: float
    ending_file_size: float
    space_saved: float
    percentage_saved: float
    all_individual_time_taken: float

    @property
    def average_time(self) -> float:
        return round(
            (self.all_individual_time_taken / self.total_number_of_encoded_files + 1), 3
        )

    @property
    def time_remaining(self) -> float:
        return round(
            (self.remaining_files_to_encode * self.average_time()) - self.starting_time,
            3,
        )


@dataclass
class variables:
    """A class that holds all useful variables"""

    input_file_path: str
    output_file_path: str
    files_to_encode: List[tuple]
    rename: bool = False
    hwacc: bool = False


@dataclass(frozen=True)
class colors:
    width = get_terminal_size((80, 20)).columns
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    ORANGE = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
