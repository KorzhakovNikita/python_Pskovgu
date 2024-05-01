

def multiply_digits(digits: list[int | float], multiplier: int | float = 2) -> list[int, float]:
    return [digit * multiplier for digit in digits]


multiply_lambda = lambda digits, multiplier: [digit * multiplier for digit in digits]


