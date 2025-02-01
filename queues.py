# queues.py
# This file contains examples and explanations for working with queues in Python.

# ================== Introduction to Queues ==================
"""
Queues are a data structure that follows the **First In, First Out (FIFO)** principle.
- The first element added to the queue is the first one to be removed.
- Queues are commonly used in scenarios like task scheduling, print spooling, and breadth-first search algorithms.
"""

# ================== Implementing Queues in Python ==================
"""
Python does not have a built-in queue data structure, but you can implement queues using:
1. Lists (not efficient for large datasets).
2. The `collections.deque` class (recommended for efficiency).
3. The `queue.Queue` class (thread-safe for multi-threaded programs).
"""

# ================== Using Lists as Queues ==================
"""
You can use a list to implement a queue, but it is not efficient for large datasets because:
- Adding or removing elements from the beginning of a list requires shifting all other elements, which is O(n) time complexity.
"""

# Example 1: Implementing a Queue Using a List
queue_list = []

# Enqueue (add elements to the end of the queue)
queue_list.append(1)
queue_list.append(2)
queue_list.append(3)
print("Queue after enqueueing:", queue_list)  # Output: [1, 2, 3]

# Dequeue (remove elements from the front of the queue)
removed_element = queue_list.pop(0)
print("Dequeued Element:", removed_element)  # Output: 1
print("Queue after dequeueing:", queue_list)  # Output: [2, 3]

# ================== Using `collections.deque` for Queues ==================
"""
The `collections.deque` class is optimized for fast appends and pops from both ends, making it ideal for implementing queues.
- `append()`: Adds an element to the end of the queue (enqueue).
- `popleft()`: Removes and returns the element from the front of the queue (dequeue).
"""

# Example 2: Implementing a Queue Using `collections.deque`
from collections import deque

queue_deque = deque()

# Enqueue (add elements to the end of the queue)
queue_deque.append(1)
queue_deque.append(2)
queue_deque.append(3)
print("Queue after enqueueing:", queue_deque)  # Output: deque([1, 2, 3])

# Dequeue (remove elements from the front of the queue)
removed_element = queue_deque.popleft()
print("Dequeued Element:", removed_element)  # Output: 1
print("Queue after dequeueing:", queue_deque)  # Output: deque([2, 3])

# ================== Using `queue.Queue` for Thread-Safe Queues ==================
"""
The `queue.Queue` class is part of Python's `queue` module and is designed for multi-threaded programs.
- It provides thread-safe operations for enqueueing and dequeueing.
- Use `put()` to enqueue and `get()` to dequeue.
"""

# Example 3: Implementing a Queue Using `queue.Queue`
import queue

queue_thread_safe = queue.Queue()

# Enqueue (add elements to the queue)
queue_thread_safe.put(1)
queue_thread_safe.put(2)
queue_thread_safe.put(3)
print("Queue after enqueueing: Not directly printable (use get())")

# Dequeue (remove elements from the queue)
removed_element = queue_thread_safe.get()
print("Dequeued Element:", removed_element)  # Output: 1

# ================== Checking if a Queue is Empty ==================
"""
You can check if a queue is empty using:
- `len(queue)` for lists and deques.
- `queue.empty()` for `queue.Queue`.
"""

# Example 4: Checking if a Queue is Empty
print("Is the list queue empty?", len(queue_list) == 0)  # Output: False
print("Is the deque queue empty?", len(queue_deque) == 0)  # Output: False
print("Is the thread-safe queue empty?", queue_thread_safe.empty())  # Output: False

# ================== Peeking at the Front of the Queue ==================
"""
Peeking allows you to view the front element of the queue without removing it.
- For lists and deques, you can access the first element using indexing.
- For `queue.Queue`, there is no built-in peek method.
"""

# Example 5: Peeking at the Front of the Queue
print("Front of the list queue:", queue_list[0])  # Output: 2
print("Front of the deque queue:", queue_deque[0])  # Output: 2

# ================== Looping Over a Queue ==================
"""
You can loop over a queue to process all its elements.
"""

# Example 6: Looping Over a Queue
print("Processing elements in the deque queue:")
for element in queue_deque:
    print(element)

# ================== EOF ==================
