import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import check_leave_balance

@pytest.mark.parametrize(
    "balance, requested, expected",
    [
        (10,5,True),
        (3,5,False),
        (10,0,False),
        (10,-2,False),
    ]
)

def test_check_leave_balance(balance, requested, expected):
    result = check_leave_balance(
balance, requested
    )

    assert result == expected