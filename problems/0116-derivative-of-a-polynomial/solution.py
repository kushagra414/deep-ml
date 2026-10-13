def poly_term_derivative(c: float, x: float, n: float) -> float:
    # c * x^n
    # nc * (x)^(n-1)
    return n*c * pow(x, n-1)