import os
from pathlib import Path
from typing import Union, Dict, Any
import pandas as pd

__all__ = [
    "is_fill_row_type",
    "is_fill_rows_type",
    "is_template_type",
    "is_dir",
    "is_empty",
    "is_output_name",
]


def is_fill_row_type(value: Union[pd.Series, Dict[str, Any]]) -> bool:
    """
    This function checks if the provided value is Union[pd.Series, Dict[str, Any]].
    In other words, it is a dictionary or a pandas Series.

    Args:
    value: The value to check.

    Returns:
    bool: True if all conditions are met, False otherwise.

    >>> is_fill_row_type(pd.Series([1, 2, 3]))
    True
    >>> is_fill_row_type({"a":1, "b":2, "c":3})
    True
    >>> is_fill_row_type(123)
    False

    """

    if isinstance(value, (pd.Series, Dict)):
        return True
    else:
        return False


def is_fill_rows_type(value: Union[pd.DataFrame, Dict[str, Dict[str, Any]]]) -> bool:
    """
    This function checks if the provided value is Union[ pd.DataFrame, Dict[str, Dict[str, Any]] ].
    In other words, it is a DataFrame or a two-layer nested dictionary.

    Args:
    value: The value to check.

    Returns:
    bool: True if all conditions are met, False otherwise.

    >>> is_fill_rows_type(pd.DataFrame(data={"A": [1, 2, 3], "B": [4, 5, 6]}))
    True
    >>> is_fill_rows_type({"A": {"1": 1}, "B": {"2": 2}})
    True
    >>> is_fill_rows_type({"A": [1, 2, 3]})
    False
    """

    if isinstance(value, pd.DataFrame):
        return True
    elif isinstance(value, Dict):
        if all(isinstance(val, Dict) for val in value.values()):
            return True

    return False


def is_template_type(filename: str) -> bool:
    """
    This function checks if the provided file matches the allowed template types.

    Args:
    filename (str): The name of the file to check.

    Returns:
    bool: True if the file extension matches the allowed extensions, False otherwise.


    >>> is_template_type("document.docx")
    True

    >>> is_template_type('c:\dev\doc.docx')
    True

    >>> is_template_type("spreadsheet.xlsx")
    True

    >>> is_template_type("image.png")
    False
    """
    allowed_extensions = [".docx", ".xlsx"]
    file_extension = Path(filename).suffix

    return file_extension in allowed_extensions


def is_dir(dir: str) -> bool:
    """
    Check if a given path is a directory.
    It accepts both relative and absolute paths.

    Args:
    dir (str): The path to check.

    Returns:
    bool: True if the path is a directory and exist, False otherwise.

    >>> is_dir("/dev/filler")
    True
    >>> is_dir("not_a_directory")
    False
    >>> is_dir("src")
    True

    """
    return os.path.isdir(dir)


def is_empty(value: Union[pd.DataFrame, pd.Series, Dict[str, Any]]) -> bool:
    """
    This function checks whether the provided value is empty.

    Args:
    value: The value to check.

    Returns:
    bool: True if the value is empty, False otherwise.

    >>> is_empty(pd.DataFrame())
    True
    >>> is_empty(pd.Series(dtype='float64'))
    True
    >>> is_empty({})
    True
    >>> is_empty({"A":1, "B":2})
    False
    """

    if isinstance(value, (pd.DataFrame, pd.Series)):
        return value.empty
    if isinstance(value, Dict):
        return not bool(value)

    return False


def is_output_name(path: str) -> bool:
    """
    Determine if the 'path' is a filename without an extension or a filename with a relative path, without an extension.

    >>> is_output_name('a001')  # A filename without an extension
    True
    >>> is_output_name('a001.xlsx')  # A filename with an extension
    False
    >>> is_output_name('data/a001')  # A filename with a relative path and without an extension
    True
    >>> is_output_name('data/a001.xlsx')  # A filename with a relative path and with an extension
    False
    >>> is_output_name('/data/a001')  # An absolute path with a filename without an extension
    False
    >>> is_output_name(1)  # Not a string
    False
    """

    # Check if 'path' is a string type
    if not isinstance(path, str):
        return False

    # Create a pathlib.Path object
    p = Path(path)

    # Check if it is an absolute path
    if os.path.isabs(path):
        return False

    # Check if the file extension is empty
    if p.suffix != '':
        return False

    return True


if __name__ == "__main__":

    import doctest

    doctest.testmod()
