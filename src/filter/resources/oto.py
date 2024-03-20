from os import path
from pathlib import Path
from typing import Any, Dict, Optional, Union

import pandas as pd

from .._utils import (
    # fill_docx, 
    # fill_xlsx,
    check_template_type,
    check_fill_datas_of_dict_type,
    check_dir,
)

from .._types import (
    FillDataCollectionTypeError,
    FillDataCollectionEmptyError,
    FillTemplateTypeError,
    FillOutputDirError,
)

__all__ = [
    'Onefillone',
]

class Onefillone:
    '''
    one row data fill into a template fill
    
    '''

    def __init__(
        self,
        data: Union[pd.DataFrame, Dict[str, Union[dict, pd.Series]]],
        template: str,
        output_dir: str,
    ):
 
        # check data param
        if not (isinstance(data, pd.DataFrame) or check_fill_datas_of_dict_type(data)):
            raise FillDataCollectionTypeError(
                "The type of the data parameter is incorrect!"
                "It is either a DataFrame or a dict with keys as strings and values as Series or dicts!"
            )
        
        if isinstance(data, pd.DataFrame):
            isempty=data.empty
        if isinstance(data, dict):
            isempty=True if not data else False
        if isempty:
            raise FillDataCollectionEmptyError("The data parameter can't be empty!")

        # check template param
        if not (path.isfile(template) or check_template_type(template)):
            raise FillTemplateTypeError(f'template parameter must be a exist file path with docx or xlsx extension!')
        
        # check output_dir param
        if not check_dir(output_dir):
            raise FillOutputDirError(f'output_dir parameter not is directory, or it is a directory but does not exist!')


    def fill(
        self
    ):
        pass

if __name__=='__main__':

    data = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
    template='tpl.docx'
    output_dir='.'   

    Onefillone(data, template, output_dir)

