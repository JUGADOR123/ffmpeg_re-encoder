from src.dataclass import colors as c
from src.dataclass import variables as v
from src.dataclass import statistics as stat
from time import time


class Statistics:
    def __init__(self) -> None:
        pass

    def renamed_statistics(self) -> None:
        print(f"{c.ORANGE}{c.BOLD}{'='*c.width}{c.RESET}")
        print(f"{c.GREEN}Total renamed files: {stat.total_files_renamed}{c.RESET}")
        print(f"{c.ORANGE}{c.BOLD}{'='*c.width}{c.RESET}")

    def probe_statistics(self) -> None:
        print(f"{c.ORANGE}{c.BOLD}{'='*c.width}{c.RESET}")
        print(
            f"{c.CYAN}{'Time taken:':25s}{c.GREEN}{round(((time()-stat.starting_time)/60),2)} Minutes{c.RESET}"
        )
        print(f"{c.CYAN}{'Total files found:':25s}{c.GREEN}{stat.total_files}{c.RESET}")
        print(
            f"{c.CYAN}{'Total files probed:':25s}{c.GREEN}{stat.total_probed_files}{c.RESET}"
        )
        print(
            f"{c.RED}{'Total failed probes:':25s}{stat.total_failed_probed_files}{c.RESET}"
        )
        print(
            f"{c.CYAN}{'Total files to encode:':25s}{c.GREEN}{stat.total_number_of_files_to_encode}{c.RESET}"
        )
        print(
            f"{c.CYAN}{'Video tracks to encode:':25s}{c.GREEN}{stat.video_tracks_to_encode}{c.RESET}"
        )
        print(
            f"{c.CYAN}{'Audio tracks to encode:':25s}{c.GREEN}{stat.audio_tracks_to_encode}{c.RESET}"
        )
        print(
            f"{c.CYAN}{'Both tracks to encode:':25s}{c.GREEN}{stat.both_tracks_to_encode}{c.RESET}"
        )
        print(
            f"{c.CYAN}{'Initial File Size:':25s}{c.GREEN}{round((stat.initial_file_size/1000),2)} GB{c.RESET}"
        )
        print(f"{c.ORANGE}{c.BOLD}{'='*c.width}{c.RESET}")

    def general_statistics(self) -> None:
        # print(f"{c.GREEN}{c.RESET}")
        print(f"{c.ORANGE}{c.BOLD}{'='*c.width}{c.RESET}")
        print(
            f"{c.GREEN}Time taken: {(stat.ending_time-stat.starting_time)/60}{c.RESET}"
        )

        print(
            f"{c.GREEN}Total number of encoded files: {stat.total_number_of_encoded_files}{c.RESET}"
        )
        print(f"{c.ORANGE}{c.BOLD}{'='*c.width}{c.RESET}")
