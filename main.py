import json
import time
import os
import shlex
import subprocess
from posixpath import splitext
cmd = "ffprobe -v quiet -print_format json -show_streams"

extensions=[".mkv",".mp4"]
video_codecs=[]
audio_codecs=[]
containers=[]
args=shlex.split(cmd)
#User input for
print("New files will be saved under the original location but with \"re-encoded\" at the end") 
#folder = input("Enter Absolute folder path: ")
folder=r"C:\Users\Jugador\Desktop\test"
rs = os.walk(folder)
for root, dirs, files in rs:
    if files:
        for file in files:
            ext=splitext(file)
            if ext[1] in extensions:
                if ext[1] not in containers:
                    containers.append(ext[1])
                filepath=os.path.join(root,file)
                args.append(filepath)
                try:
                    output=subprocess.check_output(args).decode("utf-8")
                except:
                    print(f"File errored out: {file}")
                    time.sleep(5)
                #Starts the inspection of a new file    
                print("---------------------------------------------------------------------")
                print(f"Now inspecting: {file}")
                #loads important data
                data=json.loads(output)
                #iterates through all data streams
                for stream in data["streams"]:
                    #attachment stream only has codec type most of the time
                    if stream["codec_type"]=="attachment":
                        ctype=stream["codec_type"]
                    else:
                        cname=stream["codec_name"]
                        ctype=stream["codec_type"]
                    #checks what kinds of codecs are in the whole directory
                    if ctype=="audio" and cname not in audio_codecs:
                        audio_codecs.append(cname)
                    if ctype=="video" and cname not in video_codecs:
                        video_codecs.append(cname)
                #starts actual re encoding
                if cname is not "hevc":
                    cmd2=f"ffmpeg -i \"{file}\"  -map 0:v -map 0:a -map 0:s? -c:v hevc_nvenc -crf 34 -c:a aac -c:s copy \"{ext[0]}-RE-ENCODED.mkv\""
                    args2=shlex.split(cmd2)
                    print(args2)
                    p=subprocess.Popen(args2,cwd=root)
                    result=p.wait()
                    print(result)
                else:
                    print(f"Skipped {file} as it is already hevc")

                #print(f"Output path: {root}\\{ext[0]}-RE-ENCODED{ext[1]}")
                args.pop()    
            else:
                print(f"File is not videofile: {file}")
                time.sleep(5)
print(f"Video codecs found: {video_codecs}")
print(f"Adudio codecs found: {audio_codecs}")
print(f"Containers found: {containers}")