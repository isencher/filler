import random
import numpy as np
import pandas as pd


__all__ = [
    "is_number",
    "rand_float",
    "is_empty",
]


def is_empty(value: object) -> bool:
    """
    Checks generally if a given value is empty or not.

    >>> print(is_empty(None))
    True
    >>> print(is_empty(np.nan))
    True
    >>> print(is_empty(pd.NA))
    True
    >>> print(is_empty(pd.DataFrame()))
    True
    >>> print(is_empty(pd.Series()))
    True
    >>> print(is_empty(''))
    True
    >>> print(is_empty([]))
    True
    >>> print(is_empty({}))
    True
    >>> print(is_empty('null'))
    False
    >>> print(is_empty(0))
    False

    """
    if isinstance(value, (np.ndarray, pd.DataFrame, pd.Series)):
        return value.size == 0 or value.isna().all()
    elif isinstance(value, (float, np.float32, np.float64)):
        return np.isnan(value)
    elif value is None or value == {} or value == []:
        return True
    elif isinstance(value, str) and value.strip() == "":
        return True
    elif pd.isnull(value):  # This checks for pd.NA
        return True
    return False


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
