def greet(name, age=25, city="New York"):

    print(f"Hello {name}!")
    print(f"You are {age} years old.")
    print(f"You live in {city}.")

def display_info(name, age, city, occupation="Engineer"):

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Occupation: {occupation}")

# Demonstrating default arguments
print("Default Argument Example:")
greet("Alice")  # Uses default values for age and city
greet("Bob", 30)  # Uses default value for city
greet("Charlie", 40, "Los Angeles")  # No default values used

# Demonstrating keyword arguments
print("\nKeyword Argument Example:")
display_info(name="David", age=29, city="Chicago")  # No default value for occupation
display_info(name="Eve", age=34, city="San Francisco", occupation="Data Scientist")
