# list_comprehension.py

# ================== Introduction to List Comprehension ==================
"""
List comprehensions provide a concise way to create lists in Python.
- The syntax is: [expression for item in iterable if condition]
- It’s a more readable and efficient way to generate lists compared to traditional loops.
"""

# ================== Basic List Comprehension ==================
# Example 1: Creating a list of numbers from 0 to 9
numbers = [i for i in range(10)]
print("Numbers from 0 to 9:", numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ================== List Comprehension with Condition ==================
# Example 2: Creating a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print("Even Numbers from 0 to 9:", even_numbers)  # Output: [0, 2, 4, 6, 8]

# ================== Nested List Comprehension ==================
# Example 3: Flattening a 2D list (list of lists) into a 1D list
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print("Flattened List:", flat_list)  # Output: [1, 2, 3, 4, 5, 6]

# ================== Applying Functions in List Comprehension ==================
# Example 4: Applying a function to each element of a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print("Squared Numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

# ================== List Comprehension with Multiple Conditions ==================
# Example 5: Creating a list of numbers that are divisible by 2 or 3 from 0 to 19
divisible_by_2_or_3 = [i for i in range(20) if i % 2 == 0 or i % 3 == 0]
print("Numbers divisible by 2 or 3 from 0 to 19:", divisible_by_2_or_3)  # Output: [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]

# ================== Using List Comprehension with Strings ==================
# Example 6: Extracting vowels from a string
sentence = "List comprehensions are powerful!"
vowels = [char for char in sentence if char in 'aeiou']
print("Vowels in the sentence:", vowels)  # Output: ['i', 'o', 'e', 'e', 'i', 'o', 'e']

# ================== List Comprehension with Dictionary ==================
# Example 7: Creating a dictionary with list comprehension
# A dictionary where the keys are numbers and the values are their squares
squared_dict = {i: i**2 for i in range(5)}
print("Squared Dictionary:", squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ================== List Comprehension with Set ==================
# Example 8: Creating a set of unique characters in a string
sentence = "Python programming"
unique_chars = {char for char in sentence if char.isalpha()}
print("Unique characters in the sentence:", unique_chars)  # Output: {'r', 't', 'h', 'n', 'm', 'o', 'a', 'g', 'p', 'y'}

