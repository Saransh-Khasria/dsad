class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size
    
    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()

# Recursive function to print stack elements
# from bottom to top without changing
# their order
    def printStack(self):
        
        # if stack is empty then simply return
        if self.is_empty():
            return
        x = self.peek()
    
        # pop top most element of the stack
        self.pop()
        
        # recursively call the function printStack
        self.printStack()
        
        # Print the stack element starting
        # from the bottom
        print("{} ".format(x), end = "")
        
        # Push the same element onto the stack
        # to preserve the order
        self.push(x)