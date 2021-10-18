from dataclasses import dataclass
from typing import List
from shutil import get_terminal_size


@dataclass
class statistics:
    """A class that holds all the statistic based variables"""

    total_files: int=0
    total_files_renamed: int=0
    total_failed_renamed_files: int=0
    total_probed_files: int=0
    total_failed_probed_files: int=0
    total_number_of_files_to_encode: int=0
    remaining_files_to_encode: int=0
    total_number_of_encoded_files: int=0
    total_number_of_failed_encodes: int=0
    starting_time: float=0
    ending_time: float=0
    individual_encoding_starting_time: float=0
    individual_encoding_ending_time: float=0
    initial_file_size: float=0
    ending_file_size: float=0
    space_saved: float=0
    percentage_saved: float=0
    all_individual_time_taken: float=0

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
class errors:
    """Class for error checking"""
    errors_on_rename: bool
    errors_on_probe: bool
    errors_on_encode: bool


@dataclass
class variables:
    """A class that holds all useful variables"""

    input_file_path: str
    output_file_path: str
    audio_tracks_to_encode:List[tuple]
    video_tracks_to_encode:List[tuple]
    both_tracks_to_encode:List[tuple]
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
