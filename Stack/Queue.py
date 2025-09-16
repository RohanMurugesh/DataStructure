class Queue:
    def __init__(self):
        self.items = [3]

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek from empty queue")
    
    def display(self):
        return self.items  # Returns the top item without removing it
    

# Example usage:
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue contents:", queue.display())  # Output: Queue contents: [1, 2, 3]
    
    print("Dequeued item:", queue.dequeue())   # Output: Dequeued item: 1
    print("Queue contents after dequeue:", queue.display())  # Output: Queue contents after dequeue: [2, 3]
    print("Is queue empty?", queue.is_empty()) # Output: Is queue empty? False
    print("Front item (peek):", queue.peek())  # Output: Front item (peek): 2
    print("Queue size:", queue.size())          # Output: Queue size: 2
