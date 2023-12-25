import pytest
from py_unit_automation import factorial

pytestmark = pytest.mark.factorial


@pytest.mark.parametrize("input,expected", [(1, 1), (0, 1), (2, 2), (3, 6)])
def test_factorial(input, expected):
    assert factorial(input) == expected
