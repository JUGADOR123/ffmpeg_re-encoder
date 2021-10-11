import shutil
import time
import threading
from pathlib import Path
import math
import subprocess
width = shutil.get_terminal_size((80, 20)).columns
HEADER = "\033[95m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
ORANGE = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"
animating=True





class Encode:
    def __init__(
        self,
        filepath: Path,
        filename:str,
        output_path:Path,
        acodec:list,
        vcodec:list
    ) -> None:
        self.filepath = Path(filepath)
        self.filename=filename
        self.output_path=Path(output_path)
        self.vcodec: list=vcodec
        self.acodec: list=acodec
        self._failed_files = []
        self.t=threading.Thread(target=self._animation)
        self.animating=True
    def _animation(self)->None:
        bar = [
        f"{BLUE}{BOLD}[                 ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[=                ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[===              ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[====             ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[=====            ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[======           ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[=======          ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[========         ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[ ========        ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[  ========       ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[   ========      ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[    ========     ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[     ========    ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[      ========   ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[       ========  ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[        ======== ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[         ========]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[          =======]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[           ======]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[            =====]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[             ====]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[              ===]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[               ==]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[                =]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[                 ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[                =]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[               ==]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[              ===]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[             ====]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[            =====]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[           ======]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[          =======]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[         ========]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[       ========= ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[      =========  ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[     =========   ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[   =========     ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[  =========      ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[ =========       ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[=========        ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[========         ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[=======          ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[======           ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[=====            ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[====             ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[===              ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[==               ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[=                ]{RESET}{GREEN} Encoding File...{RESET}",
        f"{BLUE}{BOLD}[                 ]{RESET}{GREEN} Encoding File...{RESET}"
        ]
        i=0
        while self.animating:
            print(bar[i % len(bar)], end="\r")
            time.sleep(0.05)
            i+=1
    def _encode(self)->bool:
        
        for (ac,vc) in zip(self.acodec,self.vcodec):
            match(ac,vc):
                case("aac","hevc"):
                    print(f"{RED}No encoding needed... Skipping{RESET}")
                    break
                case(x,"hevc"):
                    print(f"{GREEN}Re-encoding audio only...{RESET}")
                    command=f'ffmpeg -v quiet -i "{self.filepath}" -map 0 -c copy  -c:a aac -c:s srt -map_metadata 0 "{self.output_path}\ENCODED-{self.filename}.mkv"'
                    print(f"{ORANGE}Output file: {self.output_path}\ENCODED-{self.filename}.mkv{RESET}")
                    self.animating=True
                    self.t.start()
                    str_time=time.time()
                    p=subprocess.Popen(command)
                    p.wait()
                    self.animating=False
                    self.t.join()
                    print("")
                    print(f"{GREEN}Time taken to encode: {math.trunc(time.time()-str_time)} Seconds{RESET}")

                    break
                case("aac",y):
                    print(f"{GREEN}Re-encoding video only...{RESET}")
                    command=f'ffmpeg -v quiet -i "{self.filepath}" -map 0 -c copy -c:v hevc_nvenc -preset slow -x265-params crf=20 -c:s srt -map_metadata 0 "{self.output_path}\ENCODED-{self.filename}.mkv"'
                    print(f"{ORANGE}Output file: {self.output_path}\ENCODED-{self.filename}.mkv{RESET}")
                    
                    self.animating=True
                    self.t.start()
                    str_time=time.time()
                    p=subprocess.Popen(command)
                    p.wait()
                    self.animating=False
                    self.t.join()
                    print("")
                    print(f"{GREEN}Time taken to encode: {math.trunc(time.time()-str_time)} Seconds{RESET}")
                    break
                case _:
                    print(f"{GREEN}Re-encoding audio and video...{RESET}")
                    print(f"{ORANGE}Output file: {self.output_path}\ENCODED-{self.filename}.mkv{RESET}")
                    command=f'ffmpeg -v quiet -i "{self.filepath}" -map 0 -c copy -c:v hevc_nvenc -preset slow -x265-params crf=20 -c:a aac -c:s srt -map_metadata 0 "{self.output_path}\ENCODED-{self.filename}.mkv"'
                    self.animating=True
                    self.t.start()
                    str_time=time.time()
                    p=subprocess.Popen(command)
                    p.wait()
                    self.animating=False
                    self.t.join()
                    print("")
                    print(f"{GREEN}Time taken to encode: {math.trunc(time.time()-str_time)} Seconds{RESET}")

                    break
    def run(self)->None:
        self._encode()
