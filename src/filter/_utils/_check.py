
import os
from pathlib import Path
import pandas as pd

__all__ = [
    "check_fill_datas_of_dict_type",
    "check_template_type",
    "check_dir",
]

def check_fill_datas_of_dict_type(value):
    """
    This function checks if the provided value is a dictionary, and each of its values is either a dictionary or a pandas Series.
    
    Args:
    value: The value to check.

    Returns:
    bool: True if all conditions are met, False otherwise.
    
    >>> check_fill_datas_of_dict_type({"a": {"b": 1}, "c": pd.Series([1,2,3])})
    True
    >>> check_fill_datas_of_dict_type({"a": {"b": 1}, "c": [1,2,3]})
    False
    >>> check_fill_datas_of_dict_type({"a": 1})
    False
    >>> check_fill_datas_of_dict_type("a")
    False
    
    """
    
    if not isinstance(value, dict):
        return False
    for v in value.values():
        if not isinstance(v, (dict, pd.Series)):
            return False
    return True

def check_template_type(filename: str) -> bool:
    """
    This function checks if the provided file matches the allowed template types.

    Args:
    filename (str): The name of the file to check.

    Returns:
    bool: True if the file extension matches the allowed extensions, False otherwise.


    >>> check_template_type("document.docx")
    True

    >>> check_template_type('c:\dev\doc.docx')
    True

    >>> check_template_type("spreadsheet.xlsx")
    True

    >>> check_template_type("image.png")
    False
    """
    allowed_extensions = ['.docx', '.xlsx']
    file_extension = Path(filename).suffix

    return file_extension in allowed_extensions

def check_dir(dir: str) -> bool:
    '''
    Check if a given path is a directory.
    It accepts both relative and absolute paths.

    Args:
    dir (str): The path to check.

    Returns:
    bool: True if the path is a directory and exist, False otherwise.

    >>> check_dir("/dev/filler")
    True
    >>> check_dir("not_a_directory")
    False
    >>> check_dir("src")
    True
    
    '''
    return os.path.isdir(dir)

if __name__=='__main__':

    import doctest
    doctest.testmod()