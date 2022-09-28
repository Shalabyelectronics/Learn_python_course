# We will scrap THE 100 GREATEST SCIENTISTS from https://www.sapaviva.com/
import requests
from bs4 import BeautifulSoup
import re
import os
# request the page web data

def check_if_complete() -> bool:
    """
    This Function will check if we got the complate 100 scientists names
    by returning True if yes and False if not
    """
    if os.path.exists("scientists_names.txt"):
        with open("scientists_names.txt", "r") as content:
            names = content.readlines()
        if len(names) >= 100:
            return True
    return False

def check_the_web_data() -> str:
    """
    This function will check if you already requsted the web page data or not, 
    This action will save you time bt use the existed web page content otherwise
    Will create a request a new web page and save it as scientists_page.txt
    """
    if os.path.exists("scientists_page.txt"):
        with open("scientists_page.txt","r") as content:
            return content.read()
    else:
        r = requests.get("https://www.sapaviva.com/")
        with open("scientists_page.txt", "w+") as content:
            content.write(r.text)
            content.seek(0)
            return content.read()
   


def scrap_data(r):
    """
    This Function will scrap the webpage to get the scientists names
    and save them in scientists_names.txt
    """
    soup = BeautifulSoup(r, "html.parser")

    with open("scientists_names.txt", "w") as file:
        for n,link in enumerate(soup.find_all("h3"), start=1):
            try:
                all_name = link.contents[1].text.split(" ")
                just_name = " ".join(all_name[1:])
            except AttributeError as error:
                print(error)
            else:
                print(n, just_name)
                if all_name[0].isdigit():
                    continue
                file.write(f"{just_name}\n")

if __name__ == "__main__":
    if check_if_complete():
        print(f"You have the names already\nPlease check scientists_names.txt\n")
        do_check = input("Type (Y)es or (N)o : ")
        if do_check.lower() == "y":
            os.system("cat scientists_names.txt")
        else:
            os.system("clear")
    else:
        data = check_the_web_data()
        scrap_data(data)
        if check_if_complete():
            print("Great you have the complate names list.")
        else:
            print("Something went wrong you don't have the complate names list.")

