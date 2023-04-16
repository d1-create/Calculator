import time
import os
from colorama import Fore, Style, init
init()


def print_color(text, color):
    if color in Fore.__dict__:
        print(f"{getattr(Fore, color)}{text}{Style.RESET_ALL}")
    else:
        raise ValueError(f"'{color}' is not a valid color")
    



Waittime = 0.3
function = input("What do you want to do (+,-,/ or x)")
num1 = float(input("What is your first number"))
num2 = float(input("What is your second number"))


print_color("Welcome to D1-create's python calculator!", "GREEN")
time.sleep(Waittime)
os.system("clear")

while True:
    if function == "+":
        result = num1+num2
        print_color(f'{num1} + {num2} = {result}', "RED")
        break
    elif function == "-":
        result = num1-num2
        print_color(f'{num1} - {num2} = {result}', "RED")
        break
    elif function == "/":
        result = num1/num2
        break
    elif function == "x" or function == "X":
        result = num1*num2
        print_color(f'{num1} x {num2} = {result}', "RED")
        break
    else:
        print_color("Error found, forced restart of program", "RED")
        quit()