# Working with Lists (Arrays) in Python

Lists are one of the most versatile and commonly used data structures in Python. They allow you to store and manipulate collections of items efficiently. This guide covers everything you need to know about lists, from basic operations to advanced techniques.

---

## Table of Contents

1. [Introduction to Lists](#introduction-to-lists)
2. [Creating Lists](#creating-lists)
3. [Indexing Lists](#indexing-lists)
4. [Slicing Lists](#slicing-lists)
5. [Modifying Lists](#modifying-lists)
6. [Adding Elements to Lists](#adding-elements-to-lists)
7. [Deleting Elements from Lists](#deleting-elements-from-lists)
8. [List Methods](#list-methods)
9. [Looping Over Lists](#looping-over-lists)
10. [Code Examples](#code-examples)

---

## Introduction to Lists

Lists are **ordered collections of elements** that can hold items of any data type, including integers, strings, and even other lists. They are **mutable**, meaning you can add, remove, or modify elements after creation.

### Key Features of Lists:
- **Ordered**: Elements are stored in a specific order.
- **Mutable**: Elements can be changed after creation.
- **Indexed**: Elements are accessed using indices (starting from 0).
- **Dynamic**: Lists can grow or shrink in size as needed.

---

## Creating Lists

You can create a list by enclosing elements in square brackets `[]` and separating them with commas.

### Example 1: Creating a List of Strings
```python
string_list = ["John", "Mary", "Harry"]
print(string_list)  # Output: ['John', 'Mary', 'Harry']
```

### Example 2: Creating a List with Mixed Data Types
```python
mixed_list = ["Hello", 3.4, 89, "World"]
print(mixed_list)  # Output: ['Hello', 3.4, 89, 'World']
```

### Example 3: Creating a Nested List
```python
nested_list = ["Monkey", "Elephant", [3, 4, 6, 10]]
print(nested_list)  # Output: ['Monkey', 'Elephant', [3, 4, 6, 10]]
```

---

## Indexing Lists

Indexing allows you to access specific elements in a list using their position. Python uses **zero-based indexing**, meaning the first element is at index `0`.

### Example 4: Accessing Elements Using Indices
```python
pet_list = ["cat", "dog", "hamster", "goldfish", "parrot"]
print(pet_list[0])  # Output: cat (first element)
print(pet_list[-1])  # Output: parrot (last element)
```

---

## Slicing Lists

Slicing allows you to access a subset of elements from a list. The syntax is `list[start:end]`, where:
- `start` is the index of the first element to include (inclusive).
- `end` is the index of the last element to exclude (exclusive).

### Example 5: Slicing a List
```python
num_list = [1, 4, 2, 7, 5, 9, 10]
print(num_list[1:3])  # Output: [4, 2] (elements at index 1 and 2)
print(num_list[:4])   # Output: [1, 4, 2, 7] (elements from start to index 3)
print(num_list[2:])   # Output: [2, 7, 5, 9, 10] (elements from index 2 to end)
```

---

## Modifying Lists

Lists are mutable, meaning you can change their elements after creation.

### Example 6: Changing an Element in a List
```python
name_list = ["James", "Molly", "Chris", "Peter", "Kim"]
name_list[2] = "Tom"  # Replace "Chris" with "Tom"
print(name_list)  # Output: ['James', 'Molly', 'Tom', 'Peter', 'Kim']
```

### Example 7: Replacing Multiple Elements
```python
name_list[1:4] = ["Joe", "Lucy", "Kelly"]
print(name_list)  # Output: ['James', 'Joe', 'Lucy', 'Kelly', 'Kim']
```

---

## Adding Elements to Lists

You can add elements to a list using the `append()` method or the `extend()` method.

### Example 8: Adding Elements Using `append()`
```python
new_list = [34, 35, 75, "Coffee", 98.8]
new_list.append("Tea")
print(new_list)  # Output: [34, 35, 75, 'Coffee', 98.8, 'Tea']
```

### Example 9: Adding Elements Using `extend()`
```python
new_list.extend(["Cake", "Juice"])
print(new_list)  # Output: [34, 35, 75, 'Coffee', 98.8, 'Tea', 'Cake', 'Juice']
```

---

## Deleting Elements from Lists

You can delete elements from a list using the `del` keyword or the `remove()` method.

### Example 10: Deleting Elements Using `del`
```python
char_list = ["P", "y", "t", "h", "o", "n"]
del char_list[3]  # Delete the element at index 3 ('h')
print(char_list)  # Output: ['P', 'y', 't', 'o', 'n']
```

### Example 11: Deleting Elements Using `remove()`
```python
char_list.remove("t")  # Remove the first occurrence of 't'
print(char_list)  # Output: ['P', 'y', 'o', 'n']
```

---

## List Methods

Python provides several built-in methods for working with lists:

| Method     | Description                                      |
|------------|--------------------------------------------------|
| `append()` | Adds an element to the end of the list.          |
| `extend()` | Adds multiple elements to the end of the list.   |
| `insert()` | Inserts an element at a specific index.          |
| `remove()` | Removes the first occurrence of a value.         |
| `pop()`    | Removes and returns the element at a given index.|
| `index()`  | Returns the index of the first matched item.     |
| `count()`  | Returns the count of the number of items.        |
| `sort()`   | Sorts the list in ascending order.               |
| `reverse()`| Reverses the order of items in the list.         |

### Example 12: Using List Methods
```python
numbers = [5, 2, 8, 2, 1]
numbers.sort()  # Sort the list
print(numbers)  # Output: [1, 2, 2, 5, 8]

numbers.reverse()  # Reverse the list
print(numbers)  # Output: [8, 5, 2, 2, 1]
```

---

## Looping Over Lists

You can loop over a list using a `for` loop to perform operations on each element.

### Example 13: Looping Over a List
```python
food_list = ["Pizza", "Burger", "Fries", "Pasta", "Salad"]
for food in food_list:
    print(food)
```

### Example 14: Looping with Index and Value
```python
for index, food in enumerate(food_list):
    print(f"{index + 1}: {food}")
```

---

## Code Examples

For a complete set of code examples, check out the [lists_arrays.py](lists_arrays.py) file in this repository.

---

## Conclusion

Lists are a fundamental data structure in Python, and mastering them is essential for effective programming. With this guide, you should now have a solid understanding of how to create, modify, and manipulate lists in Python.

Happy coding! 🚀
