import os
import shutil

print("*"*30)
print("\n\n<<< Welcome To Send to Many Tool>>>\n\n")
print("_"*30)
add_template = input("Do you want to add a new template or choose from existed ones? (C)reat (E)xisted ")
if add_template.lower() == "e":
    print("\nChoose which Template do you want to use: \n")
    # First We are going to check if templates folder is exists>
    if os.path.exists("templates"):
        # Then We change the directory to the templates folder.
        os.chdir("templates")
        # Will Check if There any exists text templates.
        templates_list = os.listdir()
        if templates_list:
            # Will print all existed text templates.
            for index, template in enumerate(templates_list, start=1):
                print(index,template, sep="- ")
            # User should shoose one template to use.
            shosed_template = None
            
            while True:
                template_num = input("\nTemplate number is : ")
                print("_"*30,end="\n")
                if template_num.isdigit():
                    if int(template_num) - 1 in list(range(len(templates_list))):
                        shosed_template = templates_list[int(template_num) -1]
                        print(f'\nYou chosed {shosed_template} template\n')
                        print("*"*30, end="\n")
                        break
                    else:
                        print("\nWrong template number\n")
                else:
                    print("Please only Numbers!!!")
            # Now Will Check for names list        
            if os.path.exists("../names"):
                names_list = os.listdir("../names")
                if names_list:
                    # Will print all existed names list
                    print("\nChoose which names list do you want to use: \n")
                    for index, name_list in enumerate(names_list, start=1):
                        print(index,name_list, sep="- ")
                    # User should shoose one from names list
                    shosed_names_list = None
                    while True:
                        names_list_num = input("\nName list number is : ")
                        print("_"*30, end="\n")
                        if names_list_num.isdigit():
                            if int(names_list_num) - 1 in list(range(len(names_list))):    
                                shosed_names_list = names_list[int(names_list_num) -1]
                                print(f'You chosed {shosed_names_list} names list')
                                print("*"*30, end="\n")
                                break
                            else:
                                print("\nWrong number..choose again please!!")
                        else:
                            print("Please only Numbers!!!")

                    print(f"\nGreat, we are going to use {shosed_names_list} names list"\
                                f" to be use with {shosed_template}")
                        # Now After we shosed the names list and the template that we are going to use
                        # Now We creates messages.
                        # Create message folder first
                    messages_folder_name = None
                    while True:
                        # create a folder messages
                        messages_folder_name = input("\nPlease write your folder name to store all messages : ")
                        messages_folder_name = "_".join(messages_folder_name.split(" "))
                        if messages_folder_name in os.listdir(".."):
                            print("You already have this folder Choose another name please?")
                        else:
                            os.mkdir(f"../{messages_folder_name}")     
                            messages_folder_name = "_".join(messages_folder_name.split(" "))
                            break
                    # Now we will open names list that we shosed and clean it from new line skip squence
                    with open(f"../names/{shosed_names_list}", "rt", encoding="utf-8") as file:
                        names = file.readlines()
                        names_without_newline = []
                        for name in names:
                            names_without_newline.append(name[:-1])
                    # Now we will open shosen template 
                    with open(f"{shosed_template}") as file:
                        template_content = file.read()
                    for name in names_without_newline:
                        with open(f"../{messages_folder_name}/{name}.txt" , "w") as file:
                            if "[name]" not in template_content:
                                continue
                            write_content = template_content.replace("[name]",name)
                            file.write(write_content)
                    else:
                        print(f"We created All messages in {messages_folder_name}")
            else:
                os.mkdir("../names")
                print("\nPlease move your names text files to names folder that created to you"\
                        "Then rerun the script again.") 
    else:
        print("_"*30,end="\n")
        print("You do not have a template folder please rerun to script and create a new template.")
else:
    # If there is no any folder template we wil create new one.
    if os.path.exists("templates"):    
        os.chdir("templates")
        print("*"*30)
    # Then create new tmplate text file with place holder [name]
        template_name=input("What is the template name?\n")
        template_name = "_".join(template_name.split(" "))
        os.system(f"touch {template_name}.txt")
        print("Please add placeholder as [name] where you want to add the name later.\n"\
            "After creating the template press ctrl + d")
        os.system(f"cat > {template_name}.txt")
        with open(f"{template_name}.txt") as t_file:
            content = t_file.read()
        while True:    
            if "[name]" in content:
                print(f"\n\nGreet Job We detected the Place holder name in you {template_name}.txt template.")
                break
            else:
                print("\n\nWe can't detected the [name] place holder, please edit your template and add the place holder")
                os.system(f"nano {template_name}.txt")
    else:
        os.mkdir("templates")
        os.chdir("templates")
        print("*"*30)
        # Then create new tmplate text file with place holder [name]
        template_name=input("What is the template name?\n")
        template_name = "_".join(template_name.split(" "))
        os.system(f"touch {template_name}.txt")
        print("Please add placeholder as [name] where you want to add the name later.\n"\
            "After creating the template press ctrl + d")
        os.system(f"cat > {template_name}.txt")
        with open(f"{template_name}.txt") as t_file:
            content = t_file.read()
        while True:    
            if "[name]" in content:
                print(f"\n\nGreet Job We detected the Place holder name in you {template_name}.txt template.")
                break
            else:
                print("\n\nWe can't detected the [name] place holder, please edit your template and add the place holder")
                os.system(f"nano {template_name}.txt")

