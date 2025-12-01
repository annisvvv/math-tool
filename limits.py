import sympy as sp
from derivative import var, func
from sympy_commands import *

def tklimit():
    while True:
        where_limit = input("give me where the variable goes (-h for help) : ")

        if where_limit == "-h":
                print_sympy_commands()
        else:
             break
    
    while True:
        limit_side = input("give me the limit side (+ or -) or (-h for help) : ")
        
        if limit_side == "-h":
             print_sympy_commands()
        elif limit_side == "":
             limit_side == None
             break
        else:
             break
             
    return where_limit, limit_side

def limit():
    symp_variable = var()
    function_input = func()
    where_limit, limit_side = tklimit()

    try:
        if limit_side is None:
            limitt = sp.limit(function_input, symp_variable, where_limit, dir=limit_side)
            print(f"Lim {function_input} = {limitt}")
            print(f"{symp_variable} ---> {where_limit, limit_side}")
        else:
            limitt = sp.limit(function_input, symp_variable, where_limit, dir=limit_side)
            print(f"Lim {function_input} = {limitt}")
            print(f"{symp_variable} ---> {where_limit, limit_side}")

    except Exception:
        print("The function is not defined at that point please specify the limit side !")