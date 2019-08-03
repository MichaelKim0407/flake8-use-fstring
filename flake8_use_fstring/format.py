class StrFormatDetector(object):
    name = 'use-fstring-format'
    version = '1.0'

    def __init__(self, logical_line, tokens):
        self.logical_line = logical_line
        self.tokens = tokens

    def __iter__(self):
        yield 0, 'FS002 test'
