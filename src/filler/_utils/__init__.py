from ._path import create_output_dir, create_output_path
from ._utils import is_number, rand_float
from ._fill import fill_docx, fill_xlsx  # , is_empty as gen_is_empty
from ._check import (
    is_fill_row_type,
    is_fill_rows_type,
    is_template_type,
    is_dir,
    is_empty,
    # gen_is_empty,
)

__all__ = [
    "create_output_dir",
    "create_output_path",
    "is_number",
    "rand_float",
    "fill_docx",
    "fill_xlsx",
    "is_fill_row_type",
    "is_fill_rows_type",
    "is_template_type",
    "is_dir",
    "is_empty",
    # "gen_is_empty",
]
