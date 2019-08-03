import token as _token

from .base import (
    BaseLogicalLineChecker as _Base,
)


class PercentFormatDetector(_Base):
    name = 'use-fstring-percent'
    version = '1.0'

    def __getitem__(self, i: int) -> bool:
        return self.tokens[i].exact_type == _token.PERCENT

    def __call__(self, i: int) -> str:
        return "FS001 '%' operator used"

    GREEDY_OPTION_NAME = 'percent-greedy'
