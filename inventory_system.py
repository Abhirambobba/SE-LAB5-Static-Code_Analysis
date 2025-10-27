import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    if logs is None:
        logs = [] 

    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: Tried to remove {item}, but it's not in stock.")


def get_qty(item):
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        print(f"Warning: Error decoding {file}. Starting with empty inventory.")
        stock_data = {}


def save_data(file="inventory.json"):
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data, indent=4))


def print_data():
    print("--- Items Report ---")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")
    print("--------------------")


def check_low_items(threshold=5):
    return [item for item in stock_data if stock_data[item] < threshold]


def main():
    load_data()
    add_item("apple", 10)
    add_item("banana", 20)
    add_item("orange", 15)
    remove_item("apple", 3)
    remove_item("banana", 22)
    remove_item("grapes", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Banana stock: {get_qty('banana')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    print_data()


if __name__ == "__main__":
    main()