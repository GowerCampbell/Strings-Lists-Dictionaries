# dictionaries.py
# This file contains examples and explanations for working with dictionaries in Python.

# ================== Introduction to Dictionaries ==================
"""
Dictionaries are unordered collections of key-value pairs. Each key maps to a value.
- Keys must be immutable (e.g., strings, numbers, tuples).
- Values can be of any data type (e.g., integers, strings, lists, other dictionaries).
- Dictionaries are accessed using keys, not indices.
"""

# ================== Creating Dictionaries ==================
# Example 1: Creating a dictionary with string keys
profile_dict = {
    "name": "Chris",
    "surname": "Smith",
    "age": 28,
    "cell": "07714935387"
}
print("Profile Dictionary:", profile_dict)

# Example 2: Creating a dictionary with integer keys
int_key_dict = {
    1: "apple",
    2: "banana",
    3: "orange"
}
print("Integer Key Dictionary:", int_key_dict)

# Example 3: Creating a dictionary using the dict() function
int_key_list = [(1, "apple"), (2, "banana"), (3, "orange")]
int_key_dict = dict(int_key_list)
print("Dictionary from List of Tuples:", int_key_dict)

# ================== Accessing Elements from Dictionaries ==================
"""
You can access values in a dictionary using their keys.
- Use square brackets `[]` or the `get()` method.
- The `get()` method is safer as it returns `None` (or a default value) if the key is not found.
"""

# Example 4: Accessing values using keys
print("Surname:", profile_dict["surname"])  # Output: Smith
print("Cell Number:", profile_dict.get("cell"))  # Output: 07714935387

# Example 5: Accessing all keys and values
keys = profile_dict.keys()
values = profile_dict.values()
print("Keys:", keys)  # Output: dict_keys(['name', 'surname', 'age', 'cell'])
print("Values:", values)  # Output: dict_values(['Chris', 'Smith', 28, '07714935387'])

# ================== Modifying Dictionaries ==================
"""
Dictionaries are mutable, meaning you can add, update, or delete key-value pairs.
"""

# Example 6: Updating a value
profile_dict["age"] = 29  # Update the value for the key "age"
print("Updated Age:", profile_dict["age"])  # Output: 29

# Example 7: Adding a new key-value pair
profile_dict["gender"] = "male"
print("Updated Dictionary:", profile_dict)

# Example 8: Deleting a key-value pair
del profile_dict["cell"]
print("Dictionary after Deletion:", profile_dict)

# ================== Dictionary Methods ==================
"""
Python provides several built-in methods for working with dictionaries:
- `keys()`: Returns a view of all keys in the dictionary.
- `values()`: Returns a view of all values in the dictionary.
- `items()`: Returns a view of all key-value pairs as tuples.
- `get()`: Returns the value for a given key, or a default value if the key is not found.
- `pop()`: Removes and returns the value for a given key.
- `update()`: Updates the dictionary with key-value pairs from another dictionary.
- `clear()`: Removes all key-value pairs from the dictionary.
"""

# Example 9: Using dictionary methods
print("Keys:", profile_dict.keys())  # Output: dict_keys(['name', 'surname', 'age', 'gender'])
print("Values:", profile_dict.values())  # Output: dict_values(['Chris', 'Smith', 29, 'male'])
print("Items:", profile_dict.items())  # Output: dict_items([('name', 'Chris'), ('surname', 'Smith'), ('age', 29), ('gender', 'male')])

# Example 10: Using get() with a default value
print("Cell Number:", profile_dict.get("cell", "Not Found"))  # Output: Not Found

# Example 11: Using pop() to remove a key-value pair
removed_value = profile_dict.pop("gender")
print("Removed Value:", removed_value)  # Output: male
print("Dictionary after pop:", profile_dict)

# Example 12: Using update() to merge dictionaries
new_data = {"city": "London", "country": "UK"}
profile_dict.update(new_data)
print("Updated Dictionary:", profile_dict)

# Example 13: Using clear() to empty the dictionary
profile_dict.clear()
print("Cleared Dictionary:", profile_dict)  # Output: {}

# ================== Looping Over Dictionaries ==================
"""
You can loop over a dictionary to access its keys, values, or key-value pairs.
"""

# Example 14: Looping over keys
for key in int_key_dict:
    print(f"Key: {key}, Value: {int_key_dict[key]}")

# Example 15: Looping over key-value pairs
for key, value in int_key_dict.items():
    print(f"Key: {key}, Value: {value}")

# ================== Nested Dictionaries ==================
"""
Dictionaries can contain other dictionaries as values, allowing you to create complex data structures.
"""

# Example 16: Creating a nested dictionary
lecturers = {
    "Armand": {"Role": "Lecturer", "Phone Number": "0123456789"},
    "Rian": {"Role": "Lecturer", "Phone Number": "0123456789"},
    "Julian": {"Role": "Lecturer", "Phone Number": "0123456789"}
}
print("Nested Dictionary:", lecturers)

# Accessing nested dictionary values
print("Armand's Role:", lecturers["Armand"]["Role"])  # Output: Lecturer

# ================== End of File ==================
