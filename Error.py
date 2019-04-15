class Error(Exception):
    '''Base Error class for exception message'''
    pass

class inputError(Error):
    def __init__(self, msg):
        self.msg = msg

class runtimeError(Error):
    def __init__(self, msg, detail):
        self.msg = msg
        self.detail = detail

class syntaxError(Error):
    def __init__(self, msg):
        self.msg = msg

