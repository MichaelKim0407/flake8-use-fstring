import token as _token

from .base import (
    BaseGreedyLogicalLineChecker as _Base,
)
from . import __version__


class PercentFormatDetector(_Base):
    name = 'use-fstring-percent'
    version = __version__

    def __getitem__(self, i: int) -> bool:
        return self.tokens[i].exact_type == _token.PERCENT

    def __call__(self, i: int) -> str:
        return "FS001 '%' operator used"

    GREEDY_OPTION_NAME = 'percent-greedy'
