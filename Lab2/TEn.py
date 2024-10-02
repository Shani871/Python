# inventory_mgmt.py

# Initialize an empty list to store inventory items
inventory = []


def add_item(name, quantity, price):

    # Check if item already exists in inventory
    for item in inventory:
        if item['name'] == name:
            print(f"Item '{name}' already exists. Use update_quantity to change the quantity.")
            return
    # Add new item to the inventory
    inventory.append({
        'name': name,
        'quantity': quantity,
        'price': price
    })
    print(f"Item '{name}' added to inventory.")


def remove_item(name):

    for item in inventory:
        if item['name'] == name:
            inventory.remove(item)
            print(f"Item '{name}' removed from inventory.")
            return
    print(f"Item '{name}' not found in inventory.")


def update_quantity(name, quantity):

    for item in inventory:
        if item['name'] == name:
            item['quantity'] = quantity
            print(f"Quantity of '{name}' updated to {quantity}.")
            return
    print(f"Item '{name}' not found in inventory.")


def view_inventory():

    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item in inventory:
            print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")
        print()  # For a blank line after listing


if __name__ == "__main__":
    # Example of usage
    add_item("Laptop", 10, 1000.00)
    add_item("Mouse", 50, 25.50)
    view_inventory()
    update_quantity("Mouse", 60)
    view_inventory()
    remove_item("Laptop")
    view_inventory()
