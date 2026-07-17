import pytest
from calculator import add, divide


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 2, 4),
    (3, 4, 7),
    (5, 5, 10),
    (-1, -1, -2),
    (100, 100, 200),
    (1.5, 2.5, 4.0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
