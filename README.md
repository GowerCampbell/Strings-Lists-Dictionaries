Welcome to my Python programming notes repository! This repository contains detailed explanations and code examples for working with **strings**, **lists**, and **dictionaries** in Python. These notes are written in my own words and have been improved for clarity and correctness.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Flowchart Symbols](#flowchart-symbols)
3. [Data Structures](#data-structures)
   - [Lists/Arrays](#listsarrays)
   - [Dictionaries](#dictionaries)
   - [Stacks](#stacks)
   - [Queues](#queues)
4. [String Handling](#string-handling)
5. [Pseudocode](#pseudocode)
6. [List Comprehension](#list-comprehension)
7. [Copying Lists](#copying-lists)
8. [Code Files](#code-files)
9. [Bootcamp Notes from HyperionDev](#bootcamp-notes-from-hyperiondev)

---

## Introduction

This repository is a collection of my notes and code examples for understanding and working with Python's core data structures: **strings**, **lists**, and **dictionaries**. Each concept is broken down into simple explanations, accompanied by practical examples and pseudocode.

---

## Flowchart Symbols

Flowcharts are a great way to visualize algorithms and processes. Here are the symbols I use:

| Symbol | Meaning                     | Example Usage                          |
|--------|-----------------------------|----------------------------------------|
| `()`   | Start/End                   | Represents the beginning or end of a process. |
| `->`   | Arrows                      | Represents an action or calculation.   |
| `/ /`  | Input/Output                | Represents input and output operations. |
| `[ ]`  | Process                     | Represents a condition for outcomes.   |
| `↵<>↴` | Decision                    | Represents a Boolean decision (Yes/No or True/False). |

---

## Data Structures

Data structures are organized ways to store and manage data efficiently. They are essential for accessing, organizing, and modifying information easily, which is crucial for problem-solving.

### Lists/Arrays

Lists (or arrays) are ordered collections of elements. They use an **index** to access elements by their position. In programming, the first index is `0`, not `1`.

- **Key Features**:
  - Indexing: Direct access to elements using indices (e.g., `list[0]`).
  - Contiguity: Stored in adjacent memory locations for fast access.
  - Mutability: Elements can be added, removed, or modified.

- **Explanation**: [lists-arrays.md](lists-arrays.md)
- **Code Example**: [lists-arrays.py](lists-arrays.py)

### Dictionaries

Dictionaries are collections of **key-value pairs**. Each key maps to a value. Dictionaries are unordered and accessed using keys, not indices.

- **Key Features**:
  - Keys must be immutable (e.g., strings, numbers).
  - Values can be of any data type.
  - Fast lookups using keys.

- **Explanation**: [dictionaries.md](dictionaries.md)
- **Code Example**: [dictionaries.py](dictionaries.py)

### Stacks

Stacks follow the **Last In, First Out (LIFO)** principle. The last element added is the first to be removed.

- **Operations**:
  - Push: Add an element to the top.
  - Pop: Remove the top element.
  - Peek: View the top element without removing it.

- **Explanation**: [stacks.md](stacks.md)
- **Code Example**: [stacks.py](stacks.py)

### Queues

Queues follow the **First In, First Out (FIFO)** principle. The first element added is the first to be removed.

- **Operations**:
  - Enqueue: Add an element to the rear.
  - Dequeue: Remove the front element.
  - Peek: View the front element without removing it.

- **Explanation**: [queues.md](queues.md)
- **Code Example**: [queues.py](queues.py)

---

## String Handling

Strings are sequences of characters enclosed in single or double quotes. Common operations include **concatenation**, **slicing**, and **formatting**.

- **Key Methods**:
  - `strip()`: Removes whitespace from the beginning and end.
  - `replace()`: Replaces substrings.
  - `split()`: Breaks a string into a list.
  - `join()`: Combines a list into a string.

- **Explanation**: [string-handling.md](string-handling.md)
- **Code Example**: [string-handling.py](string-handling.py)

---

## Pseudocode

Pseudocode is a planning tool for algorithms. It uses simple language to describe the logic of a solution before writing actual code.

- **Example**: Finding the largest number in a list.
  ```
  SET max = first number in list
  FOR each number in list
      IF number > max THEN
          SET max = number
  END FOR
  PRINT max
  ```

- **Explanation**: [pseudocode.md](pseudocode.md)
- **Code Example**: [pseudocode.py](pseudocode.py)

---

## List Comprehension

List comprehension is a concise way to create lists by applying an operation to each element.

- **Example**: Converting strings to integers.
  ```python
  num_list = ['1', '5', '8', '14', '25', '31']
  new_num_list_ints = [int(element) for element in num_list]
  print(new_num_list_ints)  # Output: [1, 5, 8, 14, 25, 31]
  ```

- **Explanation**: [list-comprehension.md](list-comprehension.md)
- **Code Example**: [list-comprehension.py](list-comprehension.py)

---

## Copying Lists

There are two ways to copy lists: **shallow copy** and **deep copy**.

- **Shallow Copy**: Copies the outer list but not nested lists.
- **Deep Copy**: Copies all nested lists as well.

- **Explanation**: [copying-lists.md](copying-lists.md)
- **Code Example**: [copying-lists.py](copying-lists.py)

---

## Code Files

Here are the code files for each topic:

1. **Lists/Arrays**:
   - Explanation: [lists-arrays.md](lists-arrays.md)
   - Code Example: [lists-arrays.py](lists-arrays.py)
2. **Dictionaries**:
   - Explanation: [dictionaries.md](dictionaries.md)
   - Code Example: [dictionaries.py](dictionaries.py)
3. **Stacks**:
   - Explanation: [stacks.md](stacks.md)
   - Code Example: [stacks.py](stacks.py)
4. **Queues**:
   - Explanation: [queues.md](queues.md)
   - Code Example: [queues.py](queues.py)
5. **String Handling**:
   - Explanation: [string-handling.md](string-handling.md)
   - Code Example: [string-handling.py](string-handling.py)
6. **Pseudocode**:
   - Explanation: [pseudocode.md](pseudocode.md)
   - Code Example: [pseudocode.py](pseudocode.py)
7. **List Comprehension**:
   - Explanation: [list-comprehension.md](list-comprehension.md)
   - Code Example: [list-comprehension.py](list-comprehension.py)
8. **Copying Lists**:
   - Explanation: [copying-lists.md](copying-lists.md)
   - Code Example: [copying-lists.py](copying-lists.py)

---

## Bootcamp Notes from HyperionDev

This section contains my notes and tasks from the **HyperionDev Bootcamp**.

1. **Bootcamp Notes**:
   - [knotes.py](CoGrammar-BootCamp-Tasks/knotes.py)
2. **String Manipulation Task**:
   - [alternative.py](CoGrammar-BootCamp-Tasks/alternative.py)
3. **Data Structures Task**:
   - [cafe.py](CoGrammar-BootCamp-Tasks/cafe.py)


Feel free to explore, learn, and contribute! If you have any questions or suggestions, please open an issue or submit a pull request.

Happy coding! 🚀

