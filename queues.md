
# Queues in Python

This document explains how to work with queues in Python, including their implementation and usage. Queues follow the **First In, First Out (FIFO)** principle, meaning the first element added is the first one to be removed. They are commonly used in scenarios like task scheduling, print spooling, and breadth-first search algorithms.

---

## Table of Contents
1. [Introduction to Queues](#introduction-to-queues)
2. [Implementing Queues in Python](#implementing-queues-in-python)
3. [Using Lists as Queues](#using-lists-as-queues)
4. [Using `collections.deque` for Queues](#using-collectionsdeque-for-queues)
5. [Using `queue.Queue` for Thread-Safe Queues](#using-queuequeue-for-thread-safe-queues)
6. [Checking if a Queue is Empty](#checking-if-a-queue-is-empty)
7. [Peeking at the Front of the Queue](#peeking-at-the-front-of-the-queue)
8. [Looping Over a Queue](#looping-over-a-queue)

---

## Introduction to Queues

Queues are a data structure that follows the **First In, First Out (FIFO)** principle:
- The first element added to the queue is the first one to be removed.
- They are useful in scenarios like task scheduling, print spooling, and breadth-first search algorithms.

---

## Implementing Queues in Python

Python does not have a built-in queue data structure, but you can implement queues using:
1. **Lists**: Simple but inefficient for large datasets.
2. **`collections.deque`**: Optimized for fast appends and pops from both ends.
3. **`queue.Queue`**: Thread-safe for multi-threaded programs.

---

## Using Lists as Queues

Lists can be used to implement queues, but they are inefficient for large datasets because:
- Adding or removing elements from the beginning of a list requires shifting all other elements, resulting in **O(n)** time complexity.

### Example: Implementing a Queue Using a List

```python
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
```

---

## Using `collections.deque` for Queues

The `collections.deque` class is optimized for fast appends and pops from both ends, making it ideal for implementing queues.

### Example: Implementing a Queue Using `collections.deque`

```python
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
```

---

## Using `queue.Queue` for Thread-Safe Queues

The `queue.Queue` class is part of Python's `queue` module and is designed for multi-threaded programs. It provides thread-safe operations for enqueueing and dequeueing.

### Example: Implementing a Queue Using `queue.Queue`

```python
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
```

---

## Checking if a Queue is Empty

You can check if a queue is empty using:
- `len(queue)` for lists and deques.
- `queue.empty()` for `queue.Queue`.

### Example: Checking if a Queue is Empty

```python
print("Is the list queue empty?", len(queue_list) == 0)  # Output: False
print("Is the deque queue empty?", len(queue_deque) == 0)  # Output: False
print("Is the thread-safe queue empty?", queue_thread_safe.empty())  # Output: False
```

---

## Peeking at the Front of the Queue

Peeking allows you to view the front element of the queue without removing it:
- For lists and deques, use indexing (e.g., `queue[0]`).
- For `queue.Queue`, there is no built-in peek method.

### Example: Peeking at the Front of the Queue

```python
print("Front of the list queue:", queue_list[0])  # Output: 2
print("Front of the deque queue:", queue_deque[0])  # Output: 2
```

---

## Looping Over a Queue

You can loop over a queue to process all its elements.

### Example: Looping Over a Queue

```python
print("Processing elements in the deque queue:")
for element in queue_deque:
    print(element)
```

---

## Conclusion

Queues are a fundamental data structure in Python, and I can implement them using lists, `collections.deque`, or `queue.Queue` depending on your needs. I have also learned about this `deque` for efficient single-threaded programs and `queue.Queue` for thread-safe operations in multi-threaded environments.
