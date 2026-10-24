"""Divide two numbers without crashing on bad input."""


def safe_divide(a, b):
    """Return a / b, or None if the division is not possible."""
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return None


if __name__ == "__main__":
    try:
        x = float(input("First number: "))
        y = float(input("Second number: "))
    except ValueError:
        print("Please enter valid numbers.")
    else:
        print(safe_divide(x, y))
