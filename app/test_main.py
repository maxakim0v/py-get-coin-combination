import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (24, [4, 1, 1, 0]),
        (3, [3, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (30, [0, 1, 0, 1]),
        (0, [0, 0, 0, 0])

    ]
)
def test_get_coin_combination(cents, expected):
    assert get_coin_combination(cents) == expected