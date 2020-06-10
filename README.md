# flake8-use-fstring

* `master` (release)
    [![Build Status](https://travis-ci.com/MichaelKim0407/flake8-use-fstring.svg?branch=master)](https://travis-ci.com/MichaelKim0407/flake8-use-fstring)
    [![Coverage Status](https://coveralls.io/repos/github/MichaelKim0407/flake8-use-fstring/badge.svg?branch=master)](https://coveralls.io/github/MichaelKim0407/flake8-use-fstring?branch=master)
* `develop` (main)
    [![Build Status](https://travis-ci.com/MichaelKim0407/flake8-use-fstring.svg?branch=develop)](https://travis-ci.com/MichaelKim0407/flake8-use-fstring)
    [![Coverage Status](https://coveralls.io/repos/github/MichaelKim0407/flake8-use-fstring/badge.svg?branch=develop)](https://coveralls.io/github/MichaelKim0407/flake8-use-fstring?branch=develop)

Jump-start into modern Python by forcing yourself to use f-strings.

Works only with `python>=3.6`, apparently.

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

Optionally, this plugin can also check for strings that appear to be intended to be f-strings
but are missing the `f` prefix.
This check is meant to assist when converting code to use f-strings.
Due to the potential for false positives, this check (`FS003`) is disabled by default.
To enable this check,
add the `--enable-extensions=FS003` command line option,
or set `enable-extensions=FS003` in the `.flake8` config file.

The missing prefix check normally ignores strings that are using `%` or `.format` formatting,
to check those strings as well,
add the `--fstring-ignore-format` command line option,
or set `fstring-ignore-format=True` in the `.flake8` config file.
