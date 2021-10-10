import shutil


from pathlib import Path

width = shutil.get_terminal_size((80, 20)).columns
HEADER = "\033[95m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
ORANGE = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"


class Encode:
    def __init__(
        self,
        filepath: Path,
        output_path:Path,
        acodec:list,
        vcodec:list
    ) -> None:
        self.filepath = Path(filepath)
        self.output_path=Path(output_path)
        self.vcodec: list=vcodec
        self.acodec: list=acodec
        self._failed_files = []
    def _encode(self)->bool:
        for (ac,vc) in zip(self.acodec,self.vcodec):
            match(ac,vc):
                case("aac","hevc"):
                    print(f"{RED}No encoding needed... Skipping{RESET}")
                    break
                case(x,"hevc"):
                    print(f"{GREEN}Re-encoding audio only...{RESET}")
                    break
                case("aac",y):
                    print(f"{GREEN}Re-encoding video only...{RESET}")
                    break
                case _:
                    print(f"{GREEN}Re-encoding audio and video...{RESET}")
                    break
    def run(self)->None:
        self._encode()
