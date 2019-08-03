import typing as _typing
from tokenize import (
    TokenInfo as _TokenInfo,
)


class BaseLogicalLineChecker(object):
    def __init__(
            self,
            logical_line: str,
            tokens: _typing.List[_TokenInfo],
    ):
        self.logical_line = logical_line
        self.tokens = tokens

    def __getitem__(self, i: int) -> bool:
        raise NotImplementedError

    def __call__(self, i: int) -> str:
        raise NotImplementedError

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[int, str]]:
        for i in range(len(self.tokens)):
            if not self[i]:
                continue
            yield self.tokens[i].start, self(i)
