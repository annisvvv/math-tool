from derivative import *
from sympy_commands import *

print("Choose your option : " \
"1: derivate"
"2: exit" \
"-h: Show table of commands")

option = input("Option : ")

while True:
    if option == 1:
        derivate()

        choice = input("Do you want to continue : (y/n) : ")
        if choice == "n":
            break

    if option == 2:
        break

    if option == "-h":
        print_sympy_commands()
        break