import os, shutil

my_files = os.listdir()

for file in my_files:
    t = file.split(".")
    ft = t[-1]
    if os.path.exists(f"all_{ft}"):
        shutil.move(file,f"all_{ft}")
    else:
        os.mkdir(f"all_{ft}") 
        shutil.move(file,f"all_{ft}")

