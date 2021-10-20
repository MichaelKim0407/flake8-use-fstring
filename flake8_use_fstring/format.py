import token as _token

from .base import (
    BaseGreedyLogicalLineChecker as _Base,
)
from . import __version__


class StrFormatDetector(_Base):
    name = 'use-fstring-format'
    version = __version__

    def __getitem__(self, i: int) -> bool:
        token = self.tokens[i]
        if token.exact_type != _token.DOT:
            return False

        try:
            next_token = self.tokens[i + 1]
        except IndexError:  # pragma: no cover (syntax error)
            return False
        if next_token.exact_type != _token.NAME:
            return False  # pragma: no cover (syntax error)
        if next_token.string != 'format':
            return False

        return True

    def __call__(self, i: int) -> str:
        return "FS002 '.format' used"

    GREEDY_OPTION_NAME = 'format-greedy'
