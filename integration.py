from derivative import func, var
import sympy as sp

def integrate():
    symp_variable = var()
    function_input = func()
    
    integration = sp.integrate(function_input, symp_variable)

    print(f"∫{function_input} = {integration}")