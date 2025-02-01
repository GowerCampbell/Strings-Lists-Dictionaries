
# string_handling.md
This file contains examples and explanations for working with strings in Python.

## ================== Introduction to Strings ==================
Strings are sequences of characters enclosed in single or double quotes.
- Strings are immutable, meaning they cannot be changed after creation.
- Common operations include concatenation, slicing, and formatting.

## ================== Creating Strings ==================
### Example 1: Creating a string
```python
string = "Hello, World!"
print("String:", string)  # Output: Hello, World!
```

### Example 2: Creating a multi-line string
```python
multi_line_string = """This is a
multi-line
string."""
print("Multi-line String:", multi_line_string)
```

## ================== Indexing Strings ==================
Strings are indexed, meaning each character has a position (starting from 0).
- You can access individual characters using square brackets `[]`.
- Negative indices can be used to access characters from the end of the string.

### Example 3: Accessing characters using indices
```python
print("First Character:", string[0])  # Output: H
print("Last Character:", string[-1])  # Output: !
```

## ================== Slicing Strings ==================
Slicing allows you to extract a substring from a string.
- Syntax: string[start:end]
- The start index is inclusive, and the end index is exclusive.

### Example 4: Slicing a string
```python
print("Slice from index 0 to 5:", string[0:5])  # Output: Hello
print("Slice from index 7 to end:", string[7:])  # Output: World!
print("Slice from start to index 5:", string[:5])  # Output: Hello
```

## ================== String Methods ==================
Python provides many built-in methods for working with strings.
- `lower()`: Converts the string to lowercase.
- `upper()`: Converts the string to uppercase.
- `strip()`: Removes leading and trailing whitespace.
- `replace()`: Replaces a substring with another substring.
- `split()`: Splits the string into a list of substrings.
- `join()`: Combines a list of strings into a single string.

### Example 5: Using string methods
```python
text = "  Hello, World!  "
print("Lowercase:", text.lower())  # Output:   hello, world!  
print("Uppercase:", text.upper())  # Output:   HELLO, WORLD!  
print("Stripped:", text.strip())  # Output: Hello, World!
print("Replaced:", text.replace("World", "Python"))  # Output:   Hello, Python!  
print("Split:", text.split(","))  # Output: ['  Hello', ' World!  ']
print("Joined:", "-".join(["Hello", "World"]))  # Output: Hello-World
```

## ================== String Formatting ==================
String formatting allows you to insert variables into a string.
- Using `format()`: Insert variables using placeholders `{}`.
- Using f-strings: Embed variables directly into the string (Python 3.6+).

### Example 6: Using `format()` for string formatting
```python
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))  # Output: My name is Alice and I am 25 years old.
```

### Example 7: Using f-strings for string formatting
```python
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 25 years old.
```

## ================== Escape Characters ==================
Escape characters are used to include special characters in strings.
- `\n`: Newline
- `\t`: Tab
- `\\`: Backslash
- `\"`: Double quote
- `\'`: Single quote

### Example 8: Using escape characters
```python
print("Hello\nWorld!")  # Output: Hello (newline) World!
print("Hello\tWorld!")  # Output: Hello    World!
print("This is a backslash: \\")  # Output: This is a backslash: \
print("She said, \"Hello!\"")  # Output: She said, "Hello!"
```

## ================== String Building ==================
String building involves creating a string by concatenating or formatting smaller strings.
- You can use loops and conditionals to build complex strings.

### Example 9: Building a string using a loop
```python
number_builder = ""
i = 0
while i <= 50:
    if i % 2 == 0:
        number_builder += str(i) + " "
    i += 1
print("Even Numbers:", number_builder)  # Output: 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50
```

### Example 10: Building a string using list comprehension
```python
number_builder = [str(i) for i in range(0, 51, 2)]
print("Even Numbers:", " ".join(number_builder))  # Output: 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50
```
