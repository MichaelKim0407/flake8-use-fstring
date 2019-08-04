# flake8-use-fstring

[![Build Status](https://travis-ci.com/MichaelKim0407/flake8-use-fstring.svg?branch=master)](https://travis-ci.com/MichaelKim0407/flake8-use-fstring)
[![Coverage Status](https://coveralls.io/repos/github/MichaelKim0407/flake8-use-fstring/badge.svg?branch=master)](https://coveralls.io/github/MichaelKim0407/flake8-use-fstring?branch=master)

Jump-start into modern Python by forcing yourself to use f-strings.

Works only with `python>=3.6`, apparently.

## Reported Errors

* `FS001`: `%` formatting is used.

* `FS002`: `.format` formatting is used.

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
set `--percent-greedy` and `--format-greedy` in the command line,
or set `percent-greedy` and `format-greedy` in the `.flake8` config file.
