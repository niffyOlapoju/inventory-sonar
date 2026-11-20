import pytest
from src.inventory import add_item, remove_item, average_price


def test_add_item():
    assert add_item({}, "apple", 3) == {"apple": 3}


def test_add_item_invalid_name():
    with pytest.raises(ValueError):
        add_item({}, "", 1)


def test_remove_item():
    assert remove_item({"apple": 5}, "apple", 2) == {"apple": 3}


def test_average_price():
    assert average_price([2, 4]) == 3