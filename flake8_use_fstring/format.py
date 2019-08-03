import token as _token
from tokenize import (
    TokenInfo as _TokenInfo,
)

from .base import (
    BaseLogicalLineChecker as _Base,
)


class StrFormatDetector(_Base):
    name = 'use-fstring-format'
    version = '1.0'

    @staticmethod
    def match(token: _TokenInfo, last_token: _TokenInfo) -> bool:
        if token.exact_type != _token.NAME:
            return False
        if token.string != 'format':
            return False
        if last_token.exact_type != _token.DOT:
            return False
        return True

    def __getitem__(self, i: int) -> bool:
        token = self.tokens[i]
        if token.exact_type != _token.DOT:
            return False

        try:
            next_token = self.tokens[i + 1]
        except IndexError:
            return False
        if next_token.exact_type != _token.NAME:
            return False
        if next_token.string != 'format':
            return False

        return True

    def __call__(self, i: int) -> str:
        return "FS002 '.format' used"
