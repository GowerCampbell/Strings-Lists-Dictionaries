# list_comprehension.md

This file provides a detailed guide on how to use list comprehensions in Python. List comprehensions offer a concise way to create lists, and can be used with various conditions and transformations.

## ================== Introduction to List Comprehension ==================
List comprehensions provide a succinct way to create lists in Python. They allow you to transform and filter elements from an iterable (e.g., a range or a list) into a new list, in a single, readable line.

- The basic syntax of a list comprehension is:
  ```python
  [expression for item in iterable if condition]
  ```
  - `expression`: The operation to perform on each item.
  - `item`: The current item being processed from the iterable.
  - `iterable`: A collection of items to loop through (e.g., a list, range).
  - `condition`: An optional filter to include only items that meet a certain condition.

## ================== Basic List Comprehension ==================
### Example 1: Creating a List of Numbers from 0 to 9
This example demonstrates how to create a list of numbers using a list comprehension. The range function generates numbers from 0 to 9, and the comprehension collects them into a list.

```python
numbers = [i for i in range(10)]
print("Numbers from 0 to 9:", numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Explanation:
- `range(10)` generates numbers from 0 to 9.
- The comprehension `[i for i in range(10)]` adds each number to the list.

## ================== List Comprehension with Condition ==================
### Example 2: Creating a List of Even Numbers from 0 to 9
You can add a condition to filter the items in the list comprehension. In this case, only even numbers are added to the list.

```python
even_numbers = [i for i in range(10) if i % 2 == 0]
print("Even Numbers from 0 to 9:", even_numbers)  # Output: [0, 2, 4, 6, 8]
```

### Explanation:
- The condition `if i % 2 == 0` ensures only even numbers (those divisible by 2) are included in the list.

## ================== Nested List Comprehension ==================
### Example 3: Flattening a 2D List into a 1D List
List comprehensions can be nested. Here, we flatten a 2D list (a list of lists) into a 1D list.

```python
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print("Flattened List:", flat_list)  # Output: [1, 2, 3, 4, 5, 6]
```

### Explanation:
- The outer loop (`for sublist in nested_list`) iterates over each sublist in the `nested_list`.
- The inner loop (`for item in sublist`) iterates over each item in the current sublist.
- This results in a flattened list with all the elements from the nested list.

## ================== Applying Functions in List Comprehension ==================
### Example 4: Applying a Function to Each Element of a List
You can use list comprehensions to apply functions to each element in a list, such as squaring each number.

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print("Squared Numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

### Explanation:
- `num ** 2` is applied to each number in the list to square it.
- The resulting list contains the squares of the numbers in the original list.

## ================== List Comprehension with Multiple Conditions ==================
### Example 5: Numbers Divisible by 2 or 3
You can use multiple conditions in a list comprehension. In this example, the list includes numbers divisible by 2 or 3 from 0 to 19.

```python
divisible_by_2_or_3 = [i for i in range(20) if i % 2 == 0 or i % 3 == 0]
print("Numbers divisible by 2 or 3 from 0 to 19:", divisible_by_2_or_3)  
# Output: [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
```

### Explanation:
- The condition `if i % 2 == 0 or i % 3 == 0` filters for numbers divisible by either 2 or 3.

## ================== Using List Comprehension with Strings ==================
### Example 6: Extracting Vowels from a String
List comprehensions can be used to filter characters from a string. In this example, we extract all vowels from a given sentence.

```python
sentence = "List comprehensions are powerful!"
vowels = [char for char in sentence if char in 'aeiou']
print("Vowels in the sentence:", vowels)  # Output: ['i', 'o', 'e', 'e', 'i', 'o', 'e']
```

### Explanation:
- `char in 'aeiou'` checks if each character in the string is a vowel.
- The comprehension collects all the vowels from the string into a list.

## ================== List Comprehension with Dictionary ==================
### Example 7: Creating a Dictionary with List Comprehension
List comprehensions can also be used to create dictionaries. This example creates a dictionary where the keys are numbers and the values are their squares.

```python
squared_dict = {i: i**2 for i in range(5)}
print("Squared Dictionary:", squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Explanation:
- `{i: i**2 for i in range(5)}` creates a dictionary where each number from 0 to 4 is a key, and its square is the corresponding value.

## ================== List Comprehension with Set ==================
### Example 8: Creating a Set of Unique Characters in a String
List comprehensions can be used with sets to generate collections of unique elements. This example creates a set of unique alphabetic characters from a string.

```python
sentence = "Python programming"
unique_chars = {char for char in sentence if char.isalpha()}
print("Unique characters in the sentence:", unique_chars)  
# Output: {'r', 't', 'h', 'n', 'm', 'o', 'a', 'g', 'p', 'y'}
```

### Explanation:
- `{char for char in sentence if char.isalpha()}` filters out non-alphabetic characters and creates a set of unique alphabetic characters.

## ================== End of File ==================
