__all__ = [
    "FillerError",
    "ParamError",
    "FillDataCollectionTypeError",
    "FillDataCollectionEmptyError",
    "FillTemplateTypeError",
    "FillTemplateNotExistError",
    "FillOutputDirError",
]


class FillerError(Exception):
    pass


class ParamError(FillerError):
    pass


class FillDataCollectionError(ParamError):
    pass


class FillDataCollectionTypeError(FillDataCollectionError):
    """
    Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self,
        message="It should be either a DataFrame or a dict with keys as strings and values as Series or dicts!",
    ):
        self.message = message
        super().__init__(self.message)


class FillDataCollectionEmptyError(FillDataCollectionError):
    """
    Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="It should not be empty!"):
        self.message = message
        super().__init__(self.message)


class FillTemplateError(ParamError):
    pass


class FillTemplateTypeError(FillTemplateError):
    """
    Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="It should be a file path with docx or xlsx extension!"):
        self.message = message
        super().__init__(self.message)


class FillTemplateNotExistError(FillTemplateError):
    """
    Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="It does not exist!"):
        self.message = message
        super().__init__(self.message)


class FillOutputDirError(ParamError):
    """
    Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="It should be a exist directory!"):
        self.message = message
        super().__init__(self.message)


class FillOutputNameError(ParamError):
    pass
