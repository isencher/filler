import random

__all__ = [
    "is_number",
    "rand_float",
]


def is_number(str: str) -> bool:
    """
    Determine whether a string is a number, and return True if it is a number, else False
    str: str, a string that needs to be determined whether it is a number

    >>> is_number("345")
    True
    >>> is_number("345.33")
    True
    >>> is_number("abc")
    False

    """
    try:
        float(str)
        return True
    except ValueError:
        return False


def rand_float(start: float = -1, end: float = 1, point: int = 2) -> float:
    """
    generate a random floating-point number between start and end.
    param start: float, lower boundary.
    param end: float, higher boundary.
    param point: int, decimal places.
    return : float, random float between start and end.
    """

    return round(random.uniform(start, end), point)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
