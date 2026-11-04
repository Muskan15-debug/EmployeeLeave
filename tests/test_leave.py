import pytest
from app import check_leave_balance

@pytest.mark.parametrize(
    "balance, requested, expected",
    [
        (10,5,True),
        (3,5,True),
        (10,0,False),
        (10,-2,False),
    ]
)

def test_check_leave_balance(balance, requested, expected):
    result = check_leave_balance(
balance, requested
    )

    assert result == expected