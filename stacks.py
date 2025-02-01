# STACKS
# A data structure following the 'Last in, First out' (LIFO) principle
# Key Features
# Push: Adds an element to the top
# Pop: Removes the top element
# Peek: Retrieves the top element without removing it.

# Access: Restricted to the top element only.
# Efficiency: Operations are quick for both push & pop.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Adds an element to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Removes and returns the top element of the stack. Returns None if the stack is empty."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        """Retrieves the top element without removing it. Returns None if the stack is empty."""
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.stack)

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print("Top element:", stack.peek())  # Should print 30
    print("Popped element:", stack.pop())  # Should remove and print 30
    print("Stack size:", stack.size())    # Should print 2
    print("Is stack empty?", stack.is_empty())  # Should print False

    stack.pop()
    stack.pop()
    print("Is stack empty after popping all elements?", stack.is_empty())  # Should print True
