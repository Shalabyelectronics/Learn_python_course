import os

template_path = "templates/complain.txt"
names_path = "names/scientists_names.txt"

folder_name = input("Please add the folder name?")

os.mkdir(folder_name)

with open(template_path) as file:
    content = file.read()


clean_names = []
with open(names_path) as file:
    names_list = file.readlines()
    for name in names_list:
        clean_names.append(name[:-1])

os.chdir(folder_name)
for name in clean_names:
    with open(f"{name}.txt", "w") as file:
        c = content.replace("[name]",name)
        file.write(c)

print("\Done from making text files")
