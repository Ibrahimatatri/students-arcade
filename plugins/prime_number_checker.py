AUTHOR = "Ibrahim Atatri"
APP_NAME = "Prime Number Checker"


def is_prime(number):
    """Return True when number is prime and False otherwise."""
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def run():
    """Check an initial prime-number example."""
    number = 29
    result = "prime" if is_prime(number) else "not prime"
    return f"{number} is {result}."
