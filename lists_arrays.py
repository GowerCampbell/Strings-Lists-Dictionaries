# lists_arrays.py
# This file contains examples and explanations for working with lists (arrays) in Python.

# ================== Introduction to Lists ==================
"""
Lists are ordered collections of elements. They are one of the most versatile data structures in Python.
- Lists can hold elements of any data type (e.g., integers, strings, other lists).
- Lists are mutable, meaning you can add, remove, or modify elements after creation.
- Lists use indices to access elements, starting from 0.
"""

# ================== Creating Lists ==================
# Example 1: Creating a list of strings
string_list = ["John", "Mary", "Harry"]
print("String List:", string_list)  # Output: ['John', 'Mary', 'Harry']

# Example 2: Creating a list with mixed data types
mixed_list = ["Hello", 3.4, 89, "World"]
print("Mixed List:", mixed_list)  # Output: ['Hello', 3.4, 89, 'World']

# Example 3: Creating a nested list (list of lists)
nested_list = ["Monkey", "Elephant", [3, 4, 6, 10]]
print("Nested List:", nested_list)  # Output: ['Monkey', 'Elephant', [3, 4, 6, 10]]

# ================== Indexing Lists ==================
"""
Indexing allows you to access specific elements in a list using their position.
- Python uses zero-based indexing (the first element is at index 0).
- Negative indices can be used to access elements from the end of the list.
"""

# Example 4: Accessing elements using indices
pet_list = ["cat", "dog", "hamster", "goldfish", "parrot"]
print("First Element:", pet_list[0])  # Output: cat
print("Last Element:", pet_list[-1])  # Output: parrot

# ================== Slicing Lists ==================
"""
Slicing allows you to access a subset of elements from a list.
- Syntax: list[start:end]
- The start index is inclusive, and the end index is exclusive.
"""

# Example 5: Slicing a list
num_list = [1, 4, 2, 7, 5, 9, 10]
print("Slice from index 1 to 3:", num_list[1:3])  # Output: [4, 2]
print("Slice from start to index 4:", num_list[:4])  # Output: [1, 4, 2, 7]
print("Slice from index 2 to end:", num_list[2:])  # Output: [2, 7, 5, 9, 10]

# ================== Modifying Lists ==================
"""
Lists are mutable, meaning you can change their elements after creation.
"""

# Example 6: Changing an element in a list
name_list = ["James", "Molly", "Chris", "Peter", "Kim"]
name_list[2] = "Tom"  # Replace "Chris" with "Tom"
print("Modified List:", name_list)  # Output: ['James', 'Molly', 'Tom', 'Peter', 'Kim']

# Example 7: Replacing multiple elements
name_list[1:4] = ["Joe", "Lucy", "Kelly"]
print("Updated List:", name_list)  # Output: ['James', 'Joe', 'Lucy', 'Kelly', 'Kim']

# ================== Adding Elements to Lists ==================
"""
You can add elements to a list using the `append()` method or the `extend()` method.
- `append()`: Adds a single element to the end of the list.
- `extend()`: Adds multiple elements to the end of the list.
"""

# Example 8: Adding elements using append()
new_list = [34, 35, 75, "Coffee", 98.8]
new_list.append("Tea")
print("List after append:", new_list)  # Output: [34, 35, 75, 'Coffee', 98.8, 'Tea']

# Example 9: Adding elements using extend()
new_list.extend(["Cake", "Juice"])
print("List after extend:", new_list)  # Output: [34, 35, 75, 'Coffee', 98.8, 'Tea', 'Cake', 'Juice']

# ================== Deleting Elements from Lists ==================
"""
You can delete elements from a list using the `del` keyword or the `remove()` method.
- `del`: Deletes an element at a specific index.
- `remove()`: Deletes the first occurrence of a specific value.
"""

# Example 10: Deleting elements using del
char_list = ["P", "y", "t", "h", "o", "n"]
del char_list[3]  # Delete the element at index 3 ('h')
print("List after del:", char_list)  # Output: ['P', 'y', 't', 'o', 'n']

# Example 11: Deleting elements using remove()
char_list.remove("t")  # Remove the first occurrence of 't'
print("List after remove:", char_list)  # Output: ['P', 'y', 'o', 'n']

# ================== List Methods ==================
"""
Python provides several built-in methods for working with lists:
- `append()`: Adds an element to the end of the list.
- `extend()`: Adds multiple elements to the end of the list.
- `insert()`: Inserts an element at a specific index.
- `remove()`: Removes the first occurrence of a value.
- `pop()`: Removes and returns the element at a specific index.
- `index()`: Returns the index of the first occurrence of a value.
- `count()`: Returns the number of occurrences of a value.
- `sort()`: Sorts the list in ascending order.
- `reverse()`: Reverses the order of the list.
"""

# Example 12: Using list methods
numbers = [5, 2, 8, 2, 1]
numbers.sort()  # Sort the list
print("Sorted List:", numbers)  # Output: [1, 2, 2, 5, 8]

numbers.reverse()  # Reverse the list
print("Reversed List:", numbers)  # Output: [8, 5, 2, 2, 1]

# ================== Looping Over Lists ==================
"""
You can loop over a list using a `for` loop to perform operations on each element.
"""

# Example 13: Looping over a list
food_list = ["Pizza", "Burger", "Fries", "Pasta", "Salad"]
print("Food List:")
for food in food_list:
    print(food)

# Example 14: Looping with index and value
for index, food in enumerate(food_list):
    print(f"{index + 1}: {food}")

# ================== End of File ==================
