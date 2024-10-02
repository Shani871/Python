# Combined inventory management tasks

# Task 1: Create a list of prices and calculate the average price
prices = [1200, 50, 25, 300, 100]

# Step 1: Calculate the average price
average_price = sum(prices) / len(prices)

# Step 2: Print the average price
print("Average price of all products:", average_price)

# Task 2: Count the number of products whose price is above 500
# Initialize a counter for products above 500
count_above_500 = sum(1 for price in prices if price > 500)

# Print the count of products above 500
print("Number of products with price above 500:", count_above_500)

# Task 3: Remove the last product from the list and add a new product at the beginning
products = ["Laptop", "Keyboard", "Mouse", "Monitor", "Headphones"]

# Remove the last product
removed_product = products.pop()

# Print the removed product
print("Removed product:", removed_product)

# Add a new product at the beginning
new_product = "Smartphone"
products.insert(0, new_product)

# Print the updated list of products
print("Updated list of products:", products)

# Task 4: Find the index of the product with the maximum price and replace its price with a new value
# List of products and their prices
products_with_prices = [
    {"name": "Laptop", "price": 1200},
    {"name": "Keyboard", "price": 50},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 300},
    {"name": "Headphones", "price": 100}
]

# Step 1: Find the index of the product with the maximum price
max_price = -1
max_index = -1
for index, product in enumerate(products_with_prices):
    if product["price"] > max_price:
        max_price = product["price"]
        max_index = index

# Step 2: Replace the price of the product with a new value
new_price = 1500  # Example new price
products_with_prices[max_index]["price"] = new_price

# Step 3: Print the updated list of products with prices
print("Updated list of products with prices:")
for product in products_with_prices:
    print(f"{product['name']}: ${product['price']}")
