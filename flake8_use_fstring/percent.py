import token as _token
import typing as _typing
from tokenize import (
    TokenInfo as _TokenInfo,
)


class PercentFormatDetector(object):
    name = 'use-fstring-percent'
    version = '1.0'

    def __init__(
            self,
            logical_line: str,
            tokens: _typing.List[_TokenInfo],
    ):
        self.logical_line = logical_line
        self.tokens = tokens

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[int, str]]:
        for token in self.tokens:
            if token.exact_type != _token.PERCENT:
                continue
            yield token.start, f"FS001 '%' operator used"
