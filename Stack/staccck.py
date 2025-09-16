class Stack:
    def __init__(self):
        self.items = []

# Function to check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0  # Returns True if stack is empty, else False

# Function to add an item to the stack
    def push(self, item):
        self.items.append(item)  # Adds item to the top of the stack

# Function to remove and return the top item from the stack
    def pop(self):
        if self.is_empty():  # If stack is empty, return None
            print("Stack is empty, stack underflow.")
            return None
        return self.items.pop()
    
    # Function to return the top item without removing it
    def peek(self):  # 
        if self.is_empty():  # If stack is empty, 
            return None
        return self.items[-1]  # Returns the top item without removing it
   
    def size(self):
        return len(self.items)
    
    def recersive(self):
        if self.is_empty():
            return
        item = self.pop()
        self.recersive()
        print(item)
        self.push(item)
        


    # Function to display the stack contents
    def display(self):
        return self.items
    
# Example usage:
if __name__ == "__main__":    # Create a stack and perform some operations
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack contents:", stack.display())  # Output: Stack contents: [1, 2, 3]
   
    print("Popped item:", stack.pop())         # Output: Popped item: 3
    print("Stack contents after pop:", stack.display())  # Output: Stack contents after pop: [1, 2]
    print("Is stack empty?", stack.is_empty()) # Output: Is stack empty? False
    print("Top item (peek):", stack.peek())  # Output: Top item (peek): 2
    print("Stack size:", stack.size())  # Output: Stack size: 2
    stack.recersive()  # Output: 1 2