# copying_lists.md

This file demonstrates the different ways of copying lists in Python and explains the key differences between shallow and deep copies.

## ================== Introduction to Copying Lists ==================
In Python, lists are mutable, meaning that their elements can be modified. However, copying a list doesn't always behave as expected when the list contains nested elements. The two main types of copying are shallow copies and deep copies:

- **Shallow Copy**: Creates a new list, but does not recursively copy nested objects. The elements themselves are copied, but the inner objects (if any) are shared between the original and the copy.
- **Deep Copy**: Creates a completely independent copy of the list and all its nested objects. Changes to nested elements do not affect the original list.

## ================== Shallow Copying ==================
### Example 1: Using the `copy()` Method
The `copy()` method creates a shallow copy of a list. It copies the top-level elements but does not create copies of objects within the list.

```python
original_list = [1, 2, 3, 4, 5]
shallow_copy = original_list.copy()

# Modifying the shallow copy
shallow_copy[0] = 100
print("Original List:", original_list)  # Output: [1, 2, 3, 4, 5]
print("Shallow Copy:", shallow_copy)    # Output: [100, 2, 3, 4, 5]
```

### Explanation:
- The `copy()` method creates a new list, but modifying the elements of the shallow copy does not affect the original list.
- However, if the list contains mutable objects, changes to those objects will reflect in both the original and the copy.

### Example 2: Using List Slicing to Create a Shallow Copy
List slicing is another common technique for creating a shallow copy of a list.

```python
shallow_copy_slicing = original_list[:]
shallow_copy_slicing[1] = 200
print("Original List:", original_list)  # Output: [1, 2, 3, 4, 5]
print("Shallow Copy using slicing:", shallow_copy_slicing)  # Output: [1, 200, 3, 4, 5]
```

### Explanation:
- The slicing method (`[:]`) creates a shallow copy of the list. Modifying the shallow copy does not affect the original list.

## ================== Deep Copying ==================
### Example 3: Using the `copy` Module for Deep Copying
The `copy` module provides the `deepcopy()` method, which creates a completely independent copy of the list and its nested objects.

```python
import copy

original_list_with_nested = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original_list_with_nested)

# Modifying the deep copy
deep_copy[1][0] = 100
print("Original List with Nested Objects:", original_list_with_nested)  # Output: [1, [2, 3], 4]
print("Deep Copy:", deep_copy)    # Output: [1, [100, 3], 4]
```

### Explanation:
- The `deepcopy()` method creates a new list and recursively copies all objects inside it, including nested objects.
- Changes made to nested objects in the deep copy do not affect the original list.

### Example 4: Using a Loop for Manual Deep Copying
You can manually create a deep copy using a loop, especially when you need to handle nested objects.

```python
manual_deep_copy = []
for item in original_list_with_nested:
    if isinstance(item, list):
        manual_deep_copy.append(item[:])  # Create a copy of the nested list
    else:
        manual_deep_copy.append(item)

# Modifying the manual deep copy
manual_deep_copy[1][1] = 200
print("Original List with Nested Objects:", original_list_with_nested)  # Output: [1, [2, 3], 4]
print("Manual Deep Copy:", manual_deep_copy)    # Output: [1, [100, 200], 4]
```

### Explanation:
- In this example, the code manually checks for lists within the list and creates copies of any nested lists using slicing (`[:]`).
- This ensures that changes to nested lists in the copied list don't affect the original list.

## ================== Conclusion ==================
- **Shallow Copy**: Use the `copy()` method or slicing (`[:]`) for shallow copies, where changes to mutable objects in the copy may affect the original list.
- **Deep Copy**: Use `copy.deepcopy()` for full independence between the original list and its copy, especially when dealing with nested mutable objects.
- **Manual Deep Copying**: You can also manually create deep copies using loops to handle nested objects.

Understanding the differences between shallow and deep copying is important when working with mutable objects in Python.
