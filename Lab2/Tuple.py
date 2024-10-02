# a. Display the entire tuple

products = ("Laptop", 101, 999.99, 50)
# Display the entire tuple
print("Entire tuple:", products)

# b. Display the length of the tuple

length_of_tuple = len(products)
print("Length of the tuple:", length_of_tuple)

# c. Access the second element of the tuple

second_element = products[1]
print("Second element:", second_element)

# d. Find the index of a particular element in the tuple

index_of_price = products.index(999.99)
print("Index of 999.99:", index_of_price)

# e. Count the number of occurrences of a particular element in the tuple

count_of_quantity = products.count(50)
print("Count of 50:", count_of_quantity)

# f. Concatenate two tuples

additional_products = ("Mouse", 102, 25.50, 150)
# Concatenate the tuples
all_products = products + additional_products
print("Concatenated tuple:", all_products)

# g. Convert the tuple to a list

products_list = list(products)
print("Tuple as a list:", products_list)

# h. Check if a particular element is present in the tuple or not

element_exists = 101 in products
print("Is 101 in the tuple?", element_exists)


numeric_values = (999.99, 50)

max_value = max(numeric_values)
print("Maximum value:", max_value)


min_value = min(numeric_values)
print("Minimum value:", min_value)
