import pytest
from src.Circle import Circle
from src.utils import sum_two_squares
def test_utils():
    c1 = Circle(3)
    c2 = Circle(4)
    gt_sum = 21.9905
    result = sum_two_squares(c1, c2)
    assert gt_sum == result