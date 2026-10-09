
from app import calculate_total


def test_calculate_total():
    assert calculate_total(10, 5) == 50


def test_zero_quantity():
    assert calculate_total(10, 0) == 0