def test_greedy_0(test_flake8_cmd):
    test_flake8_cmd.expected_output = b"""\
tests/example.py:2:10: FS001 '%' operator used
tests/example.py:18:12: FS002 '.format' used
"""
    test_flake8_cmd.test()


def test_greedy_1(test_flake8_cmd):
    test_flake8_cmd.percent_greedy = 1
    test_flake8_cmd.format_greedy = 1
    test_flake8_cmd.expected_output = b"""\
tests/example.py:2:10: FS001 '%' operator used
tests/example.py:5:18: FS001 '%' operator used
tests/example.py:12:16: FS001 '%' operator used
tests/example.py:18:12: FS002 '.format' used
tests/example.py:21:17: FS002 '.format' used
tests/example.py:34:13: FS002 '.format' used
"""
    test_flake8_cmd.test()


def test_greedy_2(test_flake8_cmd):
    test_flake8_cmd.percent_greedy = 2
    test_flake8_cmd.format_greedy = 2
    test_flake8_cmd.expected_output = b"""\
tests/example.py:2:10: FS001 '%' operator used
tests/example.py:5:18: FS001 '%' operator used
tests/example.py:9:7: FS001 '%' operator used
tests/example.py:12:16: FS001 '%' operator used
tests/example.py:15:7: FS001 '%' operator used
tests/example.py:18:12: FS002 '.format' used
tests/example.py:21:17: FS002 '.format' used
tests/example.py:25:6: FS002 '.format' used
tests/example.py:34:13: FS002 '.format' used
tests/example.py:37:8: FS002 '.format' used
"""
    test_flake8_cmd.test()


def test_greedy_different(test_flake8_cmd):
    test_flake8_cmd.percent_greedy = 2
    test_flake8_cmd.expected_output = b"""\
tests/example.py:2:10: FS001 '%' operator used
tests/example.py:5:18: FS001 '%' operator used
tests/example.py:9:7: FS001 '%' operator used
tests/example.py:12:16: FS001 '%' operator used
tests/example.py:15:7: FS001 '%' operator used
tests/example.py:18:12: FS002 '.format' used
"""
    test_flake8_cmd.test()


def test_missing_prefix(test_flake8_cmd):
    test_flake8_cmd.enable_prefix = True
    test_flake8_cmd.expected_output = b"""\
tests/example.py:2:10: FS001 '%' operator used
tests/example.py:18:12: FS002 '.format' used
tests/example.py:49:6: FS003 f-string missing prefix
tests/example.py:50:6: FS003 f-string missing prefix
"""
    test_flake8_cmd.test()


def test_missing_prefix_ignore_format(test_flake8_cmd):
    test_flake8_cmd.enable_prefix = True
    test_flake8_cmd.ignore_format = True
    test_flake8_cmd.expected_output = b"""\
tests/example.py:2:10: FS001 '%' operator used
tests/example.py:18:5: FS003 f-string missing prefix
tests/example.py:18:12: FS002 '.format' used
tests/example.py:49:6: FS003 f-string missing prefix
tests/example.py:50:6: FS003 f-string missing prefix
"""
    test_flake8_cmd.test()
