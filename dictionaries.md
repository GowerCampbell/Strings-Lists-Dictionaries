# Working with Dictionaries in Python

Dictionaries are one of the most powerful and versatile data structures in Python. They allow you to store and manipulate collections of key-value pairs efficiently. This guide covers everything you need to know about dictionaries, from basic operations to advanced techniques.

---

## Table of Contents

1. [Introduction to Dictionaries](#introduction-to-dictionaries)
2. [Creating Dictionaries](#creating-dictionaries)
3. [Accessing Elements from Dictionaries](#accessing-elements-from-dictionaries)
4. [Modifying Dictionaries](#modifying-dictionaries)
5. [Dictionary Methods](#dictionary-methods)
6. [Looping Over Dictionaries](#looping-over-dictionaries)
7. [Nested Dictionaries](#nested-dictionaries)
8. [Code Examples](#code-examples)

---

## Introduction to Dictionaries

Dictionaries are **unordered collections of key-value pairs**. Each key maps to a value, making dictionaries ideal for storing and retrieving data efficiently.

### Key Features of Dictionaries:
- **Unordered**: Elements are not stored in a specific order.
- **Mutable**: Elements can be added, removed, or modified after creation.
- **Key-Value Pairs**: Keys must be immutable (e.g., strings, numbers, tuples), while values can be of any data type.
- **Fast Lookups**: Dictionaries are optimized for fast access using keys.

---

## Creating Dictionaries

You can create a dictionary by enclosing key-value pairs in curly braces `{}` and separating them with commas.

### Example 1: Creating a Dictionary with String Keys
```python
profile_dict = {
    "name": "Chris",
    "surname": "Smith",
    "age": 28,
    "cell": "07714935387"
}
print("Profile Dictionary:", profile_dict)
```

### Example 2: Creating a Dictionary with Integer Keys
```python
int_key_dict = {
    1: "apple",
    2: "banana",
    3: "orange"
}
print("Integer Key Dictionary:", int_key_dict)
```

### Example 3: Creating a Dictionary Using the `dict()` Function
```python
int_key_list = [(1, "apple"), (2, "banana"), (3, "orange")]
int_key_dict = dict(int_key_list)
print("Dictionary from List of Tuples:", int_key_dict)
```

---

## Accessing Elements from Dictionaries

You can access values in a dictionary using their keys. Python provides two ways to do this:
- Using square brackets `[]`.
- Using the `get()` method (safer, as it returns `None` or a default value if the key is not found).

### Example 4: Accessing Values Using Keys
```python
print("Surname:", profile_dict["surname"])  # Output: Smith
print("Cell Number:", profile_dict.get("cell"))  # Output: 07714935387
```

### Example 5: Accessing All Keys and Values
```python
keys = profile_dict.keys()
values = profile_dict.values()
print("Keys:", keys)  # Output: dict_keys(['name', 'surname', 'age', 'cell'])
print("Values:", values)  # Output: dict_values(['Chris', 'Smith', 28, '07714935387'])
```

---

## Modifying Dictionaries

Dictionaries are mutable, meaning you can add, update, or delete key-value pairs after creation.

### Example 6: Updating a Value
```python
profile_dict["age"] = 29  # Update the value for the key "age"
print("Updated Age:", profile_dict["age"])  # Output: 29
```

### Example 7: Adding a New Key-Value Pair
```python
profile_dict["gender"] = "male"
print("Updated Dictionary:", profile_dict)
```

### Example 8: Deleting a Key-Value Pair
```python
del profile_dict["cell"]
print("Dictionary after Deletion:", profile_dict)
```

---

## Dictionary Methods

Python provides several built-in methods for working with dictionaries:

| Method     | Description                                      |
|------------|--------------------------------------------------|
| `keys()`   | Returns a view of all keys in the dictionary.    |
| `values()` | Returns a view of all values in the dictionary.  |
| `items()`  | Returns a view of all key-value pairs as tuples. |
| `get()`    | Returns the value for a given key, or a default value if the key is not found. |
| `pop()`    | Removes and returns the value for a given key.   |
| `update()` | Updates the dictionary with key-value pairs from another dictionary. |
| `clear()`  | Removes all key-value pairs from the dictionary. |

### Example 9: Using Dictionary Methods
```python
print("Keys:", profile_dict.keys())  # Output: dict_keys(['name', 'surname', 'age', 'gender'])
print("Values:", profile_dict.values())  # Output: dict_values(['Chris', 'Smith', 29, 'male'])
print("Items:", profile_dict.items())  # Output: dict_items([('name', 'Chris'), ('surname', 'Smith'), ('age', 29), ('gender', 'male')])
```

### Example 10: Using `get()` with a Default Value
```python
print("Cell Number:", profile_dict.get("cell", "Not Found"))  # Output: Not Found
```

### Example 11: Using `pop()` to Remove a Key-Value Pair
```python
removed_value = profile_dict.pop("gender")
print("Removed Value:", removed_value)  # Output: male
print("Dictionary after pop:", profile_dict)
```

### Example 12: Using `update()` to Merge Dictionaries
```python
new_data = {"city": "London", "country": "UK"}
profile_dict.update(new_data)
print("Updated Dictionary:", profile_dict)
```

### Example 13: Using `clear()` to Empty the Dictionary
```python
profile_dict.clear()
print("Cleared Dictionary:", profile_dict)  # Output: {}
```

---

## Looping Over Dictionaries

You can loop over a dictionary to access its keys, values, or key-value pairs.

### Example 14: Looping Over Keys
```python
for key in int_key_dict:
    print(f"Key: {key}, Value: {int_key_dict[key]}")
```

### Example 15: Looping Over Key-Value Pairs
```python
for key, value in int_key_dict.items():
    print(f"Key: {key}, Value: {value}")
```

---

## Nested Dictionaries

Dictionaries can contain other dictionaries as values, allowing you to create complex data structures.

### Example 16: Creating a Nested Dictionary
```python
lecturers = {
    "Armand": {"Role": "Lecturer", "Phone Number": "0123456789"},
    "Rian": {"Role": "Lecturer", "Phone Number": "0123456789"},
    "Julian": {"Role": "Lecturer", "Phone Number": "0123456789"}
}
print("Nested Dictionary:", lecturers)
```

### Example 17: Accessing Nested Dictionary Values
```python
print("Armand's Role:", lecturers["Armand"]["Role"])  # Output: Lecturer
```

---

## Code Examples

For a complete set of code examples, check out the [dictionaries.py](dictionaries.py) file in this repository.

---

## Conclusion

Dictionaries are a fundamental data structure in Python, and mastering them is essential for effective programming. With this guide, you should now have a solid understanding of how to create, modify, and manipulate dictionaries in Python.

Happy coding! 🚀
