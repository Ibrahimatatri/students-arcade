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
    """Check one prime example and one non-prime example."""
    examples = (29, 30)
    results = []

    for number in examples:
        result = "prime" if is_prime(number) else "not prime"
        results.append(f"{number} is {result}")

    return "; ".join(results) + "."
