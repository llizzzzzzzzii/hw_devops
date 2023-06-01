import pytest
from main import average

@pytest.mark.parametrize(
    ('num1', 'num2', 'num3', 'result'), [
        (100, 87, 55, 80.66666666666667),
        (43, 67, 24, 44.666666666666664),
        (99, 86.13, 76, 87.04333333333334),
    ]
)
def test_calculate_average(num1,num2,num3,result):
    assert average(num1,num2,num3)==result