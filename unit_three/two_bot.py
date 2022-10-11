from random import choice
from time import sleep

def bot1():
    """This bot will return a random word"""
    words = ["Hi", "Bye", "fdsfsd"]
    return choice(words)

def bot2(word):
    """This bot will get a word from bot one and return the answer"""
    if word == "Hi":
        return "Hello, How are you?"
    elif word == "Bye":
        return "Nice to meet you,bye."
    else:
        return "I don't understand you?"


for _ in range(5):
    sleep(1.5)
    print(bot2(bot1()))


