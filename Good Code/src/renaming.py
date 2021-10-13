from pathlib import Path
import os
import shutil


HEADER = "\033[95m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
ORANGE = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"


class Rename:
    def __init__(
        self,
        base_folder: Path,
        to_remove: str,
        to_add: str,
    ) -> None:
        self.base_folder = Path(base_folder).absolute()
        self.to_remove = to_remove
        self.to_add = to_add
        self.failed = []

    def _rename(self, item: Path) -> Path:
        new_item = None
        if self.to_remove in item.name:
            try:
                new_item = item.rename(
                    item.parent /
                    item.name.replace(self.to_remove, self.to_add))
            except Exception as e:
                print(
                    f"{RED}Failed to rename {BLUE}{str(item)!r}{RED}: {ORANGE}{e}{RESET}"
                )
                self.failed.append((str(item), str(e)))
            else:
                print(
                    f"{GREEN}Renamed {BLUE}{item.name!r}{GREEN} to {BLUE}{new_item.name!r}{RESET}"
                )
        #print(f"{ORANGE}Nothing renamed!{RESET}")
        return new_item or item

    def _process_folder(self, directory: Path) -> None:
        try:
            for item in directory.iterdir():
                item = self._rename(item)
                if item.is_dir():
                    self._process_folder(item)
        except Exception as e:
            print(
                f"{RED}Failed to process {BLUE}{str(directory)!r}{RED}: {ORANGE}{e}{RESET}"
            )
            self.failed.append((str(directory), str(e)))

    def run(self) -> bool:
        self._process_folder(self.base_folder)
        width = shutil.get_terminal_size((80, 20)).columns
        if self.failed:
            print(f'{RED}{BOLD}{"=" * width}{RESET}')
            print(f"{RED}{BOLD}{'Errors occurred!'.center(width)}{RESET}")
            print(f'{RED}{BOLD}{"=" * width}{RESET}\n')
            for item, reason in self.failed:
                print(f"{RED}{item}{RESET}: {ORANGE}{reason}{RESET}")
            return True
        return False
