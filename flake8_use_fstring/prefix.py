import re as _re
import token as _token

from flake8.options.manager import (
    OptionManager as _OptionManager,
)

from .base import (
    BaseLogicalLineChecker as _Base,
)

from .utils import (
    is_text_string_token as _is_text_string_token,
)

from . import __version__

FSTRING_REGEX = _re.compile(r'^([a-zA-Z]*?[fF][a-zA-Z]*?){1}["\']')
NON_FSTRING_REGEX = _re.compile(
    r'^[a-zA-Z]*(?<!\b[rR])(?:\'\'\'|\'|"""|")'
    r'(.*?{.+?}.*)(?:\'|\'\'\'|"|""")$',
)


class MissingPrefixDetector(_Base):
    name = 'use-fstring-prefix'
    version = __version__
    ignore_format = False
    off_by_default = True

    def __getitem__(self, i: int) -> bool:
        token = self.tokens[i]
        if not _is_text_string_token(token):
            return False

        if FSTRING_REGEX.search(token.string):  # already is an f-string
            return False

        if not self.ignore_format:
            # look ahead for % or .format and skip if present
            for next_i, next_token in enumerate(self.tokens[i + 1:], i + 1):
                if next_token.exact_type == _token.STRING:
                    continue
                if next_token.exact_type == _token.PERCENT:
                    return False
                if next_token.exact_type == _token.DOT:
                    try:
                        next_token = self.tokens[next_i + 1]
                        if next_token.exact_type != _token.NAME:
                            break
                        if next_token.string == 'format':
                            return False
                    except IndexError:
                        pass
                break

        value = token.string.replace('{{', '').replace('}}', '')
        return NON_FSTRING_REGEX.search(value) is not None

    def __call__(self, i: int) -> str:
        return 'FS003 f-string missing prefix'

    @classmethod
    def add_options(cls, option_manager: _OptionManager):
        option_manager.add_option(
            f'--{cls.OPTION_NAME}',
            action='store_true',
            default=False,
            parse_from_config=True,
        )

    @classmethod
    def parse_options(cls, options):
        option_var = cls.OPTION_NAME.replace('-', '_')
        cls.ignore_format = vars(options)[option_var]

    OPTION_NAME = 'fstring-ignore-format'
