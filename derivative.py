import sympy as sp

def derivate():
    # creating the variable for sympy
    input_variable = input("give me the variable : ")
    symp_variable = sp.symbols(input_variable)

    # demand to the user to write the function
    function = input("what is your function : ")
    function_input = sp.sympify(function)

    # derivate the function
    derivative = sp.diff(function_input, symp_variable)

    print(f"f(x)' = {function_input}' = {derivative}")