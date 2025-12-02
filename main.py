from derivative import *
from sympy_commands import *
from limits import limit
from integration import integrate

print("Choose your option : \n" \
"-d: derivate\n" \
"-l: limits\n"\
"-i: integration\n"
"-h: Show table of commands\n\n" \
"To exit type exit.\n")

option = input("mth> ")

while True:
    if option == "-d":
        derivate()
        option = input("mth> ")
    
    elif option == "-l":
        limit()
        option = input("mth> ")

    elif option == "exit":
        break

    elif option == "-h":
        print_sympy_commands()
        option = input("mth> ")
     
    elif option == "-i":
        integrate()
        option = input("mth> ")

    else:
        option = input("mth> ")