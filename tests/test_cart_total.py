import pytest
import sys

sys.path.insert(0, "../src")  # Add the 'src' directory to the path
from cart_total import (
    calculate_total_cost,
    apply_discount,
    apply_tax,
    calculate_final_price,
)


def test_cart_operations():
    # Test cases for calculate_total_cost
    cart1 = [
        {"name": "item1", "price": 20.0, "quantity": 2},
        {"name": "item2", "price": 50.0, "quantity": 1},
    ]
    assert calculate_total_cost(cart1) == 90.0

    cart2 = [{"name": "item1", "price": 30.0, "quantity": 1}]
    assert calculate_total_cost(cart2) == 30.0

    cart3 = []
    assert calculate_total_cost(cart3) == 0.0

    # Test cases for apply_discount
    assert apply_discount(90.0) == 90.0  # No discount below 100
    assert apply_discount(130.0) == 117.0  # Discount applied above 100

    # Test cases for apply_tax
    assert apply_tax(90.0) == 97.2  # Tax applied to 90.0
    assert apply_tax(117.0) == 126.36  # Tax applied to 117.0

    # Test cases for calculate_final_price
    cart4 = [
        {"name": "item1", "price": 20.0, "quantity": 2},
        {"name": "item2", "price": 50.0, "quantity": 1},
    ]
    assert calculate_final_price(cart4) == 97.2  # No discount, tax applied

    cart5 = [
        {"name": "item1", "price": 50.0, "quantity": 2},
        {"name": "item2", "price": 30.0, "quantity": 1},
    ]
    assert calculate_final_price(cart5) == 126.36  # Discount applied, tax added

    cart6 = [{"name": "item1", "price": 10.0, "quantity": 5}]
    assert calculate_final_price(cart6) == 54.0  # No discount, tax applied


# Run all the tests
if __name__ == "__main__":
    pytest.main()
