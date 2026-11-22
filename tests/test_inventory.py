import pytest
from src.inventory import (
    add_item,
    remove_item,
    update_item,
    average_price,
    load_count,
)


def test_add_item():
    assert add_item({}, "apple", 3) == {"apple": 3}


def test_add_item_invalid_name():
    with pytest.raises(ValueError):
        add_item({}, "", 1)


def test_add_item_negative_quantity():
    with pytest.raises(ValueError):
        add_item({}, "apple", -1)


def test_remove_item():
    assert remove_item({"apple": 5}, "apple", 2) == {"apple": 3}


def test_remove_item_missing():
    with pytest.raises(KeyError):
        remove_item({}, "ghost", 1)


def test_update_item():
    assert update_item({}, "pear", 7) == {"pear": 7}


def test_average_price():
    assert average_price([2, 4]) == 3


def test_average_price_empty():
    assert average_price([]) == 0


def test_load_count():
    assert load_count("12") == 12
    assert load_count("abc") == 0