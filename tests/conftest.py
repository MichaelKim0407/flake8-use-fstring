import subprocess

import pytest


class TestFlake8Cmd(object):
    def __init__(self):
        self.percent_greedy = 0
        self.format_greedy = 0
        self.enable_prefix = False
        self.ignore_format = False
        self.expected_output = None

    def test(self):
        if self.expected_output is None:
            raise ValueError('expected output not provided')
        cmd = [
            'flake8',
            'tests/example.py',
            '--exclude=',
            f'--percent-greedy={self.percent_greedy}',
            f'--format-greedy={self.format_greedy}',
        ]
        if self.enable_prefix:
            cmd.append('--enable-extensions=FS003')
        if self.ignore_format:
            cmd.append('--fstring-ignore-format')
        p = subprocess.run(
            cmd,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        assert p.returncode == 1
        assert p.stdout == self.expected_output
        assert p.stderr == b''
        return p


@pytest.fixture
def test_flake8_cmd():
    return TestFlake8Cmd()
