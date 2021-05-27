class Error(Exception):
    pass


class InputParamError(Error):
    def __init__(self, message=None):
        self.message = message

    def __call__(self, *args, **kwargs):
        return self.message


class CustomError(Error):
    def __init__(self, message=None):
        self.message = message

    def __call__(self, *args, **kwargs):
        return self.message


if __name__ == "__main__":
    print(InputParamError("abc"))
