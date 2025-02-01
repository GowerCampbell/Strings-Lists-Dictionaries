
# Stack Data Structure

## Overview

A Stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means the last element added to the stack will be the first one to be removed. Stacks can be implemented using arrays, linked lists, or even through recursion.

## Key Operations

- **Push**: Adds an element to the top of the stack. This operation increases the size of the stack.
- **Pop**: Removes the top element from the stack. If the stack is empty, this operation typically returns an error or a special value like `None`.
- **Peek (or Top)**: Retrieves the top element without removing it, allowing the user to view the most recently added item.
- **is_empty**: Checks if the stack contains any elements, returning `True` if empty and `False` otherwise.
- **size**: Returns the current number of elements in the stack.

## Characteristics

- **Access Restriction**: Only the top element of the stack can be accessed directly, maintaining strict control over data flow.
- **Efficiency**: Both push and pop operations are efficient, typically with a time complexity of O(1), making stacks suitable for scenarios requiring quick access to the most recent data.
- **Memory Usage**: Depending on the implementation, stacks can be optimised for memory usage, especially when implemented with linked lists.

## Example Usage

```python
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())  # Output: 30
print(stack.pop())   # Output: 30
print(stack.size())  # Output: 2
print(stack.is_empty())  # Output: False

stack.pop()
stack.pop()
print(stack.is_empty())  # Output: True
```

## Applications

- **Function Call Management**: The call stack keeps track of active function calls in many programming languages.
- **Expression Evaluation**: Used to evaluate expressions in postfix, prefix, and infix notation.
- **Undo Mechanisms**: Commonly used in text editors and other applications to revert to previous states.
- **Syntax Parsing**: Assists in parsing syntax in compilers and interpreters.
- **Backtracking Algorithms**: Useful in algorithms like maze-solving, puzzle games, and pathfinding algorithms where backtracking is required.
- **Browser History Management**: Navigating back and forth in web browsers relies on stack data structures.

## Advantages

- Simple to implement and use.
- Fast operations due to direct access to the top element.
- Requires minimal memory overhead.

## Disadvantages

- Limited access to elements (only the top element can be accessed).
- Can lead to stack overflow if the stack exceeds the memory limit (especially in recursive implementations).


