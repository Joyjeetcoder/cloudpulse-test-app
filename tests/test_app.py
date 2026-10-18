import os
import pytest
from app import order_total


def test_order_total():
    # Deliberate assertion error only in the selected failure scenario.
    expected = 249 if os.getenv("SCENARIO") == "test_failure" else 250
    assert order_total([100, 100, 50]) == expected


def test_empty_order():
    assert order_total([]) == 0


def test_negative_price_rejected():
    with pytest.raises(ValueError, match="negative"):
        order_total([100, -5])
