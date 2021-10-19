# flake8-use-fstring

[![Release Status](https://github.com/MichaelKim0407/flake8-use-fstring/actions/workflows/python-publish.yml/badge.svg)](https://github.com/MichaelKim0407/flake8-use-fstring/releases)
[![PyPI package](https://badge.fury.io/py/flake8-use-fstring.svg)](https://pypi.org/project/flake8-use-fstring)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/flake8-use-fstring)](https://pypi.org/project/flake8-use-fstring)

* `master` (release)
    [![Build Status](https://github.com/MichaelKim0407/flake8-use-fstring/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/MichaelKim0407/flake8-use-fstring/tree/master)
    [![Coverage Status](https://coveralls.io/repos/github/MichaelKim0407/flake8-use-fstring/badge.svg?branch=master)](https://coveralls.io/github/MichaelKim0407/flake8-use-fstring?branch=master)
* `develop` (main)
    [![Build Status](https://github.com/MichaelKim0407/flake8-use-fstring/actions/workflows/test.yml/badge.svg?branch=develop)](https://github.com/MichaelKim0407/flake8-use-fstring/)
    [![Coverage Status](https://coveralls.io/repos/github/MichaelKim0407/flake8-use-fstring/badge.svg?branch=develop)](https://coveralls.io/github/MichaelKim0407/flake8-use-fstring?branch=develop)

Jump-start into modern Python by forcing yourself to use f-strings.

Works only with `python>=3.6` since it was when f-strings were introduced.

## Installation

```bash
pip install flake8-use-fstring
```

## Reported Errors

* `FS001`: `%` formatting is used.

* `FS002`: `.format` formatting is used.

* `FS003`: f-string missing prefix (ignored by default).

## Available Configurations

### `--percent-greedy` and `--format-greedy`

This plugin checks each python statement (logical line)
and see if `%` or `.format` is used.

Since flake8 is only a code style checker and not a type checker,
it's impossible to tell for sure if the value before `%` or `.format`
is a string.

Thus, greedy level is introduced to control when the plugin should report errors.

* Level 0 (default): only report error if the value before `%` or `.format` is a string literal.

* Level 1: report error if a string literal appears before `%` or `.format` anywhere in the statement.

* Level 2: report any usage of `%` or `.format`.

If the value immediately before `%` or `.format` is not a string,
using level 1 or 2 may result in false positives.
See [tests/example.py](tests/example.py) for examples.
Thus level 0 is the default level.
However, for most projects it should be reasonable to use greedy level 2 with confidence.

To set greedy levels,
set `--percent-greedy=<level>` and `--format-greedy=<level>` in the command line,
or set `percent-greedy=<level>` and `format-greedy=<level>` in the `.flake8` config file.

### `--enable-extensions=FS003` and `--fstring-ignore-format`

This plugin can also check for strings that appear to be f-strings but don't have the `f` prefix.

Due to the potential for false positives, this check (`FS003`) is disabled by default.
To enable this check,
add the `--enable-extensions=FS003` command line option,
or set `enable-extensions=FS003` in the `.flake8` config file.

**NOTE**:
If you use the `--ignore` option of `flake8`, the default ignore list will be overwritten.
See [`--ignore`](https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-ignore)
vs [`--extend-ignore`](https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-extend-ignore).

The missing prefix check normally ignores strings that are using `%` or `.format` formatting.
To check those strings as well,
add the `--fstring-ignore-format` command line option,
or set `fstring-ignore-format=True` in the `.flake8` config file.
