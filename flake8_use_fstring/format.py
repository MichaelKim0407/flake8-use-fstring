import token as _token
import typing as _typing
from tokenize import (
    TokenInfo as _TokenInfo,
)


class StrFormatDetector(object):
    name = 'use-fstring-format'
    version = '1.0'

    def __init__(
            self,
            logical_line: str,
            tokens: _typing.List[_TokenInfo],
    ):
        self.logical_line = logical_line
        self.tokens = tokens

    @staticmethod
    def match(token: _TokenInfo, last_token: _TokenInfo) -> bool:
        if token.exact_type != _token.NAME:
            return False
        if token.string != 'format':
            return False
        if last_token.exact_type != _token.DOT:
            return False
        return True

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[int, str]]:
        last_token = None
        for token in self.tokens:
            if self.match(token, last_token):
                yield last_token.start, f"FS002 '.format' used"
            last_token = token
