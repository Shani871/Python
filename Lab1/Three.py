# Combined dictionary operations with student details

# Task 1: Add three more students to the dictionary
students = {
    "John": {"age": 20, "major": "Computer Science", "grade": "A"},
    "Alice": {"age": 21, "major": "Engineering", "grade": "B"},
    "Bob": {"age": 19, "major": "Mathematics", "grade": "B+"}
}

# Adding new students
students["Eva"] = {"age": 22, "major": "Physics", "grade": "A-"}
students["Michael"] = {"age": 20, "major": "Biology", "grade": "A"}
students["Sophia"] = {"age": 21, "major": "History", "grade": "B"}

# Print the updated dictionary
print("Updated student dictionary:")
print(students)

# Task 2: Display all the keys in the dictionary
print("\nKeys in the dictionary:")
for key in students.keys():
    print(key)

# Task 3: Display all the values in the dictionary
print("\nValues in the dictionary:")
for value in students.values():
    print(value)

# Task 4: Update the address of a student (e.g., John)
students["John"]["address"] = "123 Main St"
students["Alice"]["address"] = "456 Elm St"
students["Bob"]["address"] = "789 Oak St"
students["Eva"]["address"] = "567 Pine St"
students["Michael"]["address"] = "321 Maple St"
students["Sophia"]["address"] = "654 Cedar St"

# Update John's address
new_address = "101 Sunset Blvd"
students["John"]["address"] = new_address
print(f"\nThe address of John has been updated to {new_address}")

# Task 5: Remove a student (e.g., Bob)
removed_student = students.pop("Bob", None)
if removed_student:
    print(f"\nSuccessfully removed Bob from the dictionary.")
else:
    print(f"\nStudent 'Bob' not found in the dictionary.")

# Print the updated dictionary
print("\nUpdated student dictionary after removal:")
print(students)

# Task 6: Sort the dictionary by keys and display the sorted dictionary
sorted_students_by_key = {key: students[key] for key in sorted(students)}
print("\nSorted dictionary by keys:")
for key, value in sorted_students_by_key.items():
    print(f"{key}: {value}")

# Task 7: Sort the dictionary by values (age) and display the sorted dictionary
sorted_students_by_age = dict(sorted(students.items(), key=lambda item: item[1]["age"]))
print("\nSorted dictionary by values (age):")
for key, value in sorted_students_by_age.items():
    print(f"{key}: {value}")

# Task 8: Find the length of the dictionary
dict_length = len(students)
print(f"\nThe length of the dictionary 'students' is: {dict_length}")

# Task 9: Check if a key is present in the dictionary or not
key_to_check = "Bob"
if key_to_check in students:
    print(f"\n{key_to_check} is present in the dictionary.")
else:
    print(f"\n{key_to_check} is not present in the dictionary.")

# Task 10: Clear the dictionary and display it
students.clear()
print("\nCleared dictionary:")
print(students)
