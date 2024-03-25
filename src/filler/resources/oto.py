from os import path
from pathlib import Path
from typing import Any, Dict, Optional, Union

import pandas as pd

from .._utils import (
    fill_docx, 
    fill_xlsx,
    is_fill_row_type,
    is_fill_rows_type,
    is_template_type,
    is_dir,
    is_empty,
)

from .._types import (
    FillDataCollectionTypeError,
    FillDataCollectionEmptyError,
    FillTemplateTypeError,
    FillTemplateNotExistError,
    FillOutputDirError,
)

__all__ = [
    'RowsTemplateFiller',
]

class RowTemplateFiller:
    '''
    one row data fill into a template fill
    
    '''   
    def __init__(
        self,
        data: Union[pd.Series, Dict[str, Any]],
        template: str,
        output_dir: str,
    ):
        # check data param
        if not is_fill_row_type(data):
            raise FillDataCollectionTypeError(
                "The type of the data parameter is incorrect!\n"
                "It is either a Series or a dictionary!"
            )
        if is_empty(data):
            raise FillDataCollectionEmptyError(
                "the value of data parameter is empty!"
            )
        
        # check template param
        check_template(template)
        # check output_dir param
        check_outputdir(output_dir)
        
        self.data = data
        self.template = template
        self.output_dir = output_dir
        self.extension = template[-4:]
        
        fillers = {
            'docx': fill_docx, 
            'xlsx': fill_xlsx,
        }
        
        self.filler = fillers[self.extension]
        
        
    def fill(self, fname:str='a001'):
        output_path = path.join(self.output_dir, f'{fname}.{self.extension}')
        self.filler(
            self.data,
            self.template,
            output_path
        )

class RowsTemplateFiller:
    '''
    list data fill into a template fill one by one
    
    '''

    def __init__(
        self,
        data: Union[pd.DataFrame, Dict[str, Union[dict, pd.Series]]],
        template: str,
        output_dir: str,
    ):
 
        # check data param
        if not (isinstance(data, pd.DataFrame) or is_fill_rows_type(data)):
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
        check_template(template)
        
        # check output_dir param
        check_outputdir(output_dir)

    
    def fill(
        self
    ):
        pass


def check_template(template:str):
    if not (path.isfile(template) or is_template_type(template)):
        raise FillTemplateTypeError(f'{template} must be a file path with docx or xlsx extension!')
    if not path.exists(template):
        raise FillTemplateNotExistError(f'{template} does not exist!')  

def check_outputdir(output_dir:str):
    if not is_dir(output_dir):
        raise FillOutputDirError(f'output_dir parameter not is a directory, or it is a directory but does not exist!')
