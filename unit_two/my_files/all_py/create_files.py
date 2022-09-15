import os

file_types = ["jpg",\
        "gif", "pdf",\
        "docx", "txt"]

for file in file_types:
    for n in range(11):
        os.system(f"touch {n}.{file}")
