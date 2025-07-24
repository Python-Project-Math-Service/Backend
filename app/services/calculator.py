
def calculate_pow(base: float, exponent: float) -> float:
    return base ** exponent


def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


def calculate_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Negative index not allowed")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
