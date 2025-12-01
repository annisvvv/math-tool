import sympy as sp
from sympy_commands import *

def derivate():

    while True:
        # creating the variable for sympy
        input_variable = input("give me the variable (-h for help) : ")

        if input_variable == "-h":
            print_sympy_commands()
        else:
            symp_variable = sp.symbols(input_variable)
            break

    while True:
        # demand to the user to write the function
        function = input("what is your function (-h for help) : ")

        if function == "-h":
            print_sympy_commands()
        else:
            function_input = sp.sympify(function)
            break

    # derivate the function
    derivative = sp.diff(function_input, symp_variable)

    print(f"f(x)' = {function_input}' = {derivative}")