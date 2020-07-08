import pytest

from twenty_four import lib as module


@pytest.mark.parametrize(
    'numbers, expected',
    [
        ([8, 3, 8, 3], ['8 dividedby (3 minus (8 dividedby 3))']),
    ]
)
def test_get_solutions(numbers, expected):
    actual = module.get_solutions(numbers)

    assert actual == expected
