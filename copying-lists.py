# copying_lists.py

# ================== Introduction to Copying Lists ==================
"""
In Python, lists are mutable, meaning their content can be changed. 
When copying lists, it's important to understand the differences between shallow and deep copies.

- A shallow copy creates a new list, but it does not create copies of nested objects.
- A deep copy creates a completely independent copy of the list and all its nested objects.
"""

# ================== Shallow Copying ==================
# Example 1: Using the `copy()` method
original_list = [1, 2, 3, 4, 5]
shallow_copy = original_list.copy()

# Modifying the shallow copy
shallow_copy[0] = 100
print("Original List:", original_list)  # Output: [1, 2, 3, 4, 5]
print("Shallow Copy:", shallow_copy)    # Output: [100, 2, 3, 4, 5]

# Explanation:
# The shallow copy creates a new list, but modifying elements in the shallow copy doesn't affect the original list.
# However, if the list contains mutable objects (like lists), changes to those objects would reflect in both lists.

# Example 2: Using list slicing to create a shallow copy
shallow_copy_slicing = original_list[:]
shallow_copy_slicing[1] = 200
print("Original List:", original_list)  # Output: [1, 2, 3, 4, 5]
print("Shallow Copy using slicing:", shallow_copy_slicing)  # Output: [1, 200, 3, 4, 5]

# ================== Deep Copying ==================
# Example 3: Using the `copy` module for deep copying
import copy

original_list_with_nested = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original_list_with_nested)

# Modifying the deep copy
deep_copy[1][0] = 100
print("Original List with Nested Objects:", original_list_with_nested)  # Output: [1, [2, 3], 4]
print("Deep Copy:", deep_copy)    # Output: [1, [100, 3], 4]

# Explanation:
# The `deepcopy()` method from the `copy` module creates a completely independent copy of the list and all its nested objects.
# Modifying the nested objects in the deep copy does not affect the original list.

# Example 4: Using a loop for deep copying (manual method)
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

# ================== Conclusion ==================
"""
- Use the `copy()` method or slicing to create shallow copies when the list doesn't contain mutable objects.
- Use `copy.deepcopy()` for deep copying lists that contain nested mutable objects, ensuring full independence.
- The `copy()` method and slicing only create shallow copies, which means changes to nested objects affect both lists.
- A deep copy creates completely independent copies of both the list and its nested objects.
"""

