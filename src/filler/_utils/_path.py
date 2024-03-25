from typing import Union, Literal
from pandas import Timestamp
from datetime import datetime
import os

__all__ = [
    "create_output_dir",
    "create_output_path",
]


def create_output_dir(pre:str='out', parentdir:str=os.getcwd()):
    '''
    Create an output directory, and return the created output directory if successful, or False if failed.

    pre: str, prefix for the directory name, the suffix is filled by the current timestamp string
    parentdir: str, the parent directory to create the output directory, default is the current directory
    
    example:
        create_output_dir() #  create a subdirectory like "out_202312190844" 
                            #  in the current directory
        create_output_dir(parentdir="/src") # create a subdirectory like "out_202312190844" 
                                            # in the src directory under the current disk root directory
        create_output_dir(parentdir="src")  # create a subdirectory like "out_202312190844" 
                                            # in the src directory under the current directory
        create_output_dir(parentdir="src/filter")   # create a subdirectory like "out_202312190844" 
                                                    # in the src/filter directory under the current directory    

    >>> True if create_output_dir() is not False else False
    True

    '''
    # Generate a timestamp string with the current time
    timestamp = get_curtimestr()

    # Concatenate the prefix and timestamp to form the new directory name
    dirname = f'{pre}_{timestamp}'

    # Combine the parent directory path and the new directory name to form the full path
    output_dir = os.path.join(parentdir, dirname)

    try:
        # Create the new directory
        os.makedirs(output_dir, exist_ok=True)
        return output_dir
    except Exception as e:
        print(f"Exception occurred while making directory: {e}")
        return False

def create_output_path(
        file:str='f001', 
        ext: Union[str, Literal['xlsx', 'docx']]='xlsx', 
        dir:str=os.getcwd(),
    )->str:

    '''
    Create an full output path, and return the created output path
    
    file: str, file name of path, default is "a001"
    ext: str, extension name of file, only accept "xlsx" or "docx", default is "xlsx"
    dir: str, output directory, default is current directory
    
    >>> os.path.basename(create_output_path())
    'f001.xlsx'
    >>> os.path.dirname(create_output_path())==os.getcwd()
    True
    ''' 
    return os.path.join(dir, f'{file}.{ext}')

def get_curtimestr()->str:
    '''
    Produce a string containing the current date and time 
    following the pattern "yyyymmddhhmmss".

    >>> is_valid_timestamp(get_curtimestr())
    True

    '''
    return Timestamp.now().strftime('%Y%m%d%H%M%S')

def is_valid_timestamp(timestamp_str):
    '''
    Determine whether the given string is a timestamp string

    >>> is_valid_timestamp("202312190844")
    True

    '''

    try:
        # 尝试将字符串按照你给的格式(年月日小时分钟秒)解析为日期时间
        # 如果字符串能被成功解析,说明它是一个有效的日期时间
        datetime.strptime(timestamp_str, '%Y%m%d%H%M%S')
        return True
    except ValueError:
        # 如果在解析过程中产生了 ValueError 异常
        # 说明字符串不能被解析为一个有效的日期时间
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    



