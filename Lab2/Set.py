# Initialize two inventory sets
inventory1 = set()
inventory2 = set()

# a. Use the add() method to add items to the inventory set
inventory1.add('Laptop')
inventory1.add('Mouse')
inventory1.add('Keyboard')
print("Inventory 1 after adding items:", inventory1)

# b. Use the remove() method to remove an item from the inventory set
inventory1.remove('Mouse')  # Will raise KeyError if 'Mouse' is not present
print("Inventory 1 after removing 'Mouse':", inventory1)

# c. Use the clear() method to empty the inventory set
inventory1.clear()
print("Inventory 1 after clearing:", inventory1)

# d. Use the update() method to add multiple items to the inventory set
inventory2.update(['Monitor', 'Printer', 'Scanner'])
print("Inventory 2 after updating with multiple items:", inventory2)

# e. Use the intersection() method to find the common items between two inventory sets
common_items = inventory2.intersection({'Printer', 'Keyboard'})
print("Common items between inventory2 and another set:", common_items)

# f. Use the difference() method to find the items that are in one inventory set but not in the other
inventory3 = {'Monitor', 'Mouse', 'Keyboard'}
difference_items = inventory3.difference(inventory2)
print("Items in inventory3 but not in inventory2:", difference_items)

# g. Use the union() method to combine two inventory sets into one
combined_inventory = inventory2.union(inventory3)
print("Combined inventory:", combined_inventory)

# h. Use the copy() method to make a copy of the inventory set
inventory_copy = combined_inventory.copy()
print("Copy of the combined inventory:", inventory_copy)

# i. Use the pop() method to remove and return an arbitrary item from the inventory set
if combined_inventory:  # Check if the set is not empty
    removed_item = combined_inventory.pop()
    print("Removed item:", removed_item)
    print("Inventory after popping an item:", combined_inventory)
else:
    print("Inventory is empty, nothing to pop.")

# j. Use the discard() method to remove an item from the inventory set if it is present
# Do not raise an error if the item is not present
combined_inventory.discard('Printer')
print("Inventory after discarding 'Printer':", combined_inventory)

# Attempt to discard an item that is not in the set
combined_inventory.discard('NonexistentItem')
print("Inventory after discarding 'NonexistentItem':", combined_inventory)
