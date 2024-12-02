class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self): # check if the stack is empty
        return len(self.items) == 0

    def push(self, item): # add an element to the top of the stack
        self.items.append(item)

    def pop(self): # remove and return the top (last) element from the stack
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1] # return (show) the element at the top (end)
        else:
            raise IndexError("Peek operation on empty stack")

    def size(self): # return the length (size) of the stack
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)        # Output: [1, 2, 3]
print(stack.pop())  # Output: 3
print(stack.peek()) # Output: 2
print(stack.size()) # Output: 2
