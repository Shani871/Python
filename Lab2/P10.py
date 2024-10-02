# Define a dictionary to hold the shopping cart items
shopping_cart = {}

def add_item(item_name, item_price):

    if item_name in shopping_cart:
        print(f"{item_name} is already in the cart. Updating price.")
    shopping_cart[item_name] = item_price
    print(f"Added {item_name} to the cart with price ${item_price:.2f}")

def remove_item(item_name):

    if item_name in shopping_cart:
        del shopping_cart[item_name]
        print(f"Removed {item_name} from the cart.")
    else:
        print(f"{item_name} is not in the cart.")

def view_cart():
    """
    Displays the items in the shopping cart and the total cost.
    """
    if not shopping_cart:
        print("Your shopping cart is empty.")
    else:
        print("\nItems in your shopping cart:")
        total_cost = 0
        for item_name, item_price in shopping_cart.items():
            print(f"{item_name}: ${item_price:.2f}")
            total_cost += item_price
        print(f"\nTotal cost: ${total_cost:.2f}")

# Sample usage of the shopping cart functions
add_item("Apple", 0.99)
add_item("Banana", 1.29)
add_item("Milk", 2.49)
view_cart()
remove_item("Banana")
view_cart()
