class StatusError(BaseException):
    """Raised when the requested URL returns an error status code"""
    def __init__(self, message):
        super().__init__(message)


class NetworkError(BaseException):
    """Raised when no connection is able to be established due to network issues"""
    def __init__(self, message):
        super().__init__(message)