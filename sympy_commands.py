def print_sympy_commands():
    commands = {
        "Basic Operations": [
            "x**2              -> square",
            "x**3              -> cube",
            "1/x               -> reciprocal",
            "abs(x)            -> absolute value"
        ],
        "Roots": [
            "sqrt(x)           -> square root",
            "x**(1/2)          -> square root",
            "x**(1/3)          -> cube root",
            "(expr)**(1/n)     -> n-th root"
        ],
        "Trigonometric": [
            "sin(x)", "cos(x)", "tan(x)",
            "asin(x)", "acos(x)", "atan(x)",
            "sec(x)", "csc(x)", "cot(x)"
        ],
        "Exponential / Logarithmic": [
            "exp(x)            -> e^x",
            "log(x)            -> natural logarithm ln(x)",
            "log(x, 10)        -> logarithm base 10",
            "log(x, a)         -> logarithm base a"
        ],
        "Algebraic": [
            "expand(expr)      -> expand expression",
            "factor(expr)      -> factor expression",
            "simplify(expr)    -> simplify expression",
            "solve(eq, x)      -> solve equation for x"
        ],
        "Calculus": [
            "diff(expr, x)     -> derivative",
            "integrate(expr,x) -> integral",
            "limit(expr,x,a)   -> limit as x -> a",
            "limit(expr,x,oo)  -> limit as x -> +∞",
            "limit(expr,x,-oo) -> limit as x -> -∞"
        ],
        "Special Symbols": [
            "pi                -> π",
            "E                 -> Euler's number e",
            "I                 -> imaginary unit √-1",
            "oo                -> +infinity",
            "-oo               -> -infinity",
            "zoo               -> complex infinity",
            "nan               -> undefined (not a number)",
            "GoldenRatio       -> φ (1.618…)",
            "gamma             -> Euler–Mascheroni constant"
        ],
        "Variables & Sets": [
            "symbols('x y')    -> declare variables",
            "Interval(0,1)     -> interval [0,1]",
            "Integers          -> ℤ",
            "Reals             -> ℝ",
            "EmptySet          -> ∅"
        ]
    }

    print("\n===== SymPy Command Reference =====")
    for category, items in commands.items():
        print(f"\n--- {category} ---")
        for item in items:
            print("  " + item)
    print("\n===================================\n")
