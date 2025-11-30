from derivative import *
from sympy_commands import *

print("Choose your option : \n" \
"-d: derivate\n" \
"-h: Show table of commands\n\n" \
"To exit type exit.\n")

option = input("mth> ")

while True:
    if option == "-d":
        derivate()
        option = input("mth> ")

    if option == "exit":
        break

    if option == "-h":
        print_sympy_commands()
        option = input("mth> ")
    
    else:
        option = input("mth> ")