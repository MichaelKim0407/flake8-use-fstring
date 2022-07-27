import typing as _typing

from tokenize import (
    TokenInfo as _TokenInfo,
)

from flake8.options.manager import (
    OptionManager as _OptionManager,
)

from flake8_use_fstring.utils import (
    is_text_string_token as _is_text_string_token,
)

Flake8Output = _typing.Tuple[_typing.Tuple[int, int], str]


class BaseLogicalLineChecker(object):
    def __init__(
            self,
            logical_line: str,
            tokens: _typing.List[_TokenInfo],
    ):
        self.logical_line = logical_line
        self.tokens = tokens

    def __getitem__(self, i: int) -> bool:
        raise NotImplementedError  # pragma: no cover

    def __call__(self, i: int) -> str:
        raise NotImplementedError  # pragma: no cover

    def __iter__(self) -> _typing.Iterator[Flake8Output]:
        for i in range(len(self.tokens)):
            if not self[i]:
                continue
            yield self.tokens[i].start, self(i)


class BaseGreedyLogicalLineChecker(BaseLogicalLineChecker):
    def __iter__(self) -> _typing.Iterator[Flake8Output]:
        met_string = False

        for i in range(len(self.tokens)):
            if _is_text_string_token(self.tokens[i]):
                met_string = True

            if not self[i]:
                continue

            if self.greedy == self.NO_GREEDY:
                # only if last token is string
                if i == 0:  # cannot use IndexError because -1 is a valid index
                    continue  # pragma: no cover (syntax error)
                if not _is_text_string_token(self.tokens[i - 1]):
                    continue

            elif self.greedy == self.GREEDY_MET_STRING:
                # only if there has been a string to the left
                if not met_string:
                    continue

            else:
                # match everything
                pass

            yield self.tokens[i].start, self(i)

    GREEDY_OPTION_NAME = None

    NO_GREEDY = '0'
    GREEDY_MET_STRING = '1'
    GREEDY_ANY = '2'
    GREEDY_CHOICES = (
        NO_GREEDY,
        GREEDY_MET_STRING,
        GREEDY_ANY,
    )

    @classmethod
    def add_options(cls, option_manager: _OptionManager):
        option_manager.add_option(
            f'--{cls.GREEDY_OPTION_NAME}',
            default=cls.NO_GREEDY, choices=cls.GREEDY_CHOICES,
            parse_from_config=True,
        )

    GREEDY_OPTION_VAR = None

    @classmethod
    def parse_options(cls, options):
        greedy_option_var = (
                cls.GREEDY_OPTION_VAR
                or cls.GREEDY_OPTION_NAME.replace('-', '_')
        )
        cls.greedy = vars(options)[greedy_option_var]
