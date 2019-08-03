import subprocess

import pytest


class TestFlake8Cmd(object):
    def __init__(self):
        self.percent_greedy = None
        self.format_greedy = None
        self.expected_output = None

    def test(self):
        if self.expected_output is None:
            raise ValueError('expected output not provided')
        cmd = ['flake8', 'tests/example.py', '--exclude=']
        if self.percent_greedy is not None:
            cmd.append(f'--percent-greedy={self.percent_greedy}')
        if self.format_greedy is not None:
            cmd.append(f'--format-greedy={self.format_greedy}')
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
