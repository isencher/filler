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
    is_output_name,
)

from .._types import (
    FillDataCollectionTypeError,
    FillDataCollectionEmptyError,
    FillTemplateTypeError,
    FillTemplateNotExistError,
    FillOutputDirError,
    FillOutputNameError,
)

__all__ = [
    "RowTemplateFiller",
]


class RowTemplateFiller:
    """
    one row data fill into a template fill

    """

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
                "the value of data parameter is empty!")

        # check template param
        check_template(template)
        # check output_dir param
        check_outputdir(output_dir)

        self.data = data
        self.template = template
        self.output_dir = output_dir
        self.extension = template[-4:]

        fillers = {
            "docx": fill_docx,
            "xlsx": fill_xlsx,
        }

        self.filler = fillers[self.extension]

        self._output_name = 'a001'

    @property
    def output_name(self) -> str:
        return self._output_name

    @output_name.setter
    def output_name(self, value: str) -> str:
        if not is_output_name(value):
            raise FillOutputNameError(
                'The value of output_name parameter is incorrect!'
                'It should be a file name without an extension, with or without a relative directory!'
            )
        self._output_name = value

    def fill(self):
        output_path = path.join(
            self.output_dir, f"{self.output_name}.{self.extension}")
        self.filler(self.data, self.template, output_path)


def check_template(template: str):
    if not (path.isfile(template) or is_template_type(template)):
        raise FillTemplateTypeError(
            f"{template} must be a file path with docx or xlsx extension!"
        )
    if not path.exists(template):
        raise FillTemplateNotExistError(f"{template} does not exist!")


def check_outputdir(output_dir: str):
    if not is_dir(output_dir):
        raise FillOutputDirError(
            f"output_dir parameter not is a directory, or it is a directory but does not exist!"
        )
