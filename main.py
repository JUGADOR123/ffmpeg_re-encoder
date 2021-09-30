import os
from posixpath import splitext


#User input for 
folder = input("Enter Absolute folder path: ")

print(f" Home dir: {folder}")
total = 0
rs = os.walk(folder)
for root, dirs, files in rs:
    print("---------------------------------------------------------------------")
    print(f"Parent folder: {os.path.basename(root)}")
    # print(f" Root folder: {root}")
    formatted = ", ".join(dirs)
    print(f"    Subfolders: {formatted}" if dirs else "   No subfolder")
    if files:
        for file in files:
            splitted = splitext(file)
            print(f"        File: {splitted[0]} Extension: {splitted[1]}")
            total = total + 1
print(total)
