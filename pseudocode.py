# ================== Introduction to Pseudocode ==================
"""
Pseudocode is a way to describe the logic of a program or algorithm using plain language.
- It is not tied to any specific programming language.
- It helps in planning and communicating the structure of a program before writing actual code.
"""

# ================== Basic Pseudocode Structure ==================
"""
Pseudocode typically includes:
1. Input: Describing the data or values that the program will receive.
2. Process: Describing the steps or logic to manipulate the data.
3. Output: Describing the result or output of the program.
"""

# ================== Example 1: Finding the Largest Number in a List ==================
"""
Problem: Find the largest number in a list of numbers.

Pseudocode:
1. SET max = first number in the list
2. FOR each number in the list
   a. IF number > max THEN
      i. SET max = number
3. END FOR
4. PRINT max
"""

# Python Implementation
numbers = [5, 2, 8, 2, 1]
max_num = numbers[0]  # Step 1
for num in numbers:  # Step 2
    if num > max_num:  # Step 2a
        max_num = num  # Step 2a.i
print("Largest Number:", max_num)  # Step 4

# ================== Example 2: Reversing a List ==================
"""
Problem: Reverse a list of elements.

Pseudocode:
1. SET reversed_list = empty list
2. FOR i FROM length of list - 1 DOWN TO 0
   a. APPEND list[i] to reversed_list
3. END FOR
4. PRINT reversed_list
"""

# Python Implementation
original_list = [100, 2, -50]
reversed_list = []  # Step 1
for i in range(len(original_list) - 1, -1, -1):  # Step 2
    reversed_list.append(original_list[i])  # Step 2a
print("Reversed List:", reversed_list)  # Step 4

# ================== Example 3: Checking if a Number is Prime ==================
"""
Problem: Check if a given number is prime.

Pseudocode:
1. INPUT number
2. IF number <= 1 THEN
   a. PRINT "Not a prime number"
   b. EXIT
3. FOR i FROM 2 TO square root of number
   a. IF number % i == 0 THEN
      i. PRINT "Not a prime number"
      ii. EXIT
4. PRINT "Prime number"
"""

# Python Implementation
import math

number = 29  # Step 1
if number <= 1:  # Step 2
    print("Not a prime number")  # Step 2a
else:
    is_prime = True
    for i in range(2, int(math.sqrt(number)) + 1):  # Step 3
        if number % i == 0:  # Step 3a
            is_prime = False
            print("Not a prime number")  # Step 3a.i
            break
    if is_prime:
        print("Prime number")  # Step 4

# ================== Example 4: Calculating the Sum of a List ==================
"""
Problem: Calculate the sum of all numbers in a list.

Pseudocode:
1. SET total = 0
2. FOR each number in the list
   a. SET total = total + number
3. END FOR
4. PRINT total
"""

# Python Implementation
numbers = [1, 2, 3, 4, 5]
total = 0  # Step 1
for num in numbers:  # Step 2
    total += num  # Step 2a
print("Total Sum:", total)  # Step 4

# ================== Example 5: Finding the Minimum Number in a List ==================
"""
Problem: Find the smallest number in a list of numbers.

Pseudocode:
1. SET min = first number in the list
2. FOR each number in the list
   a. IF number < min THEN
      i. SET min = number
3. END FOR
4. PRINT min
"""

# Python Implementation
numbers = [5, 2, 8, 2, 1]
min_num = numbers[0]  # Step 1
for num in numbers:  # Step 2
    if num < min_num:  # Step 2a
        min_num = num  # Step 2a.i
print("Smallest Number:", min_num)  # Step 4

# ================== Example 6: Sorting a List (Bubble Sort) ==================
"""
Problem: Sort a list of numbers in ascending order using the Bubble Sort algorithm.

Pseudocode:
1. SET n = length of list
2. FOR i FROM 0 TO n - 1
   a. FOR j FROM 0 TO n - i - 1
      i. IF list[j] > list[j + 1] THEN
         A. SWAP list[j] and list[j + 1]
3. END FOR
4. PRINT list
"""

# Python Implementation
numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)  # Step 1
for i in range(n):  # Step 2
    for j in range(0, n - i - 1):  # Step 2a
        if numbers[j] > numbers[j + 1]:  # Step 2a.i
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # Step 2a.i.A
print("Sorted List:", numbers)  # Step 4
