def add_item(inventory, name, qty):
    if name == "":
        raise ValueError("Invalid item name")
    if qty < 0:
        raise ValueError("Invalid quantity")
    inventory[name] = inventory.get(name, 0) + qty
    return inventory


def remove_item(inventory, name, qty):
    if name == "":
        raise ValueError("Invalid item name")
    if qty < 0:
        raise ValueError("Invalid quantity")
    if name not in inventory:
        raise KeyError("Item not found")
    inventory[name] -= qty
    return inventory


def update_item(inventory, name, qty):
    if name == "":
        raise ValueError("Invalid item name")
    if qty < 0:
        raise ValueError("Invalid quantity")
    inventory[name] = qty
    return inventory


def average_price(prices):
    if not prices:
        return 0
    return sum(prices) / len(prices)


def load_count(text):
    unused = 0
    try:
        return int(text)
    except:
        return 0