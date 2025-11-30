def print_sympy_commands():
    commands = {
        "Basic Operations": [
            "x**2        -> square",
            "x**3        -> cube",
            "1/x         -> reciprocal",
            "abs(x)      -> absolute value"
        ],
        "Roots": [
            "sqrt(x)     -> square root",
            "x**(1/2)    -> square root",
            "x**(1/3)    -> cube root",
            "(x+1)**(1/n)-> n-th root"
        ],
        "Trigonometric": [
            "sin(x)", "cos(x)", "tan(x)",
            "asin(x)", "acos(x)", "atan(x)"
        ],
        "Exponential / Logarithmic": [
            "exp(x)      -> e^x",
            "log(x)      -> natural log",
            "log(x, 10)  -> log base 10"
        ],
        "Algebraic": [
            "expand(expr)    -> expand expression",
            "factor(expr)    -> factor expression",
            "simplify(expr)  -> simplify expression"
        ],
        "Calculus": [
            "diff(expr, x)    -> derivative",
            "integrate(expr)  -> integral",
            "limit(expr, x, a)-> limit at x=a"
        ],
        "Misc": [
            "pi          -> π",
            "E           -> e",
            "oo          -> infinity",
            "symbols('x y') -> declare variables"
        ]
    }

    for category, items in commands.items():
        print(f"\n=== {category} ===")
        for item in items:
            print("  " + item)
