class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            print(f"Queue is full. Cannot enqueue {item}.")
        else:
            self.queue += [item]  # manual add
            print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            item = self.queue[0]
            self.queue = self.queue[1:]  # manual remove
            print(f"Dequeued: {item}")
            return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        return self.queue[0]
    # 
    def size(self):
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue (front -> rear):", self.queue)
        return self.queue
    
# Example usage:
q = Queue(max_size=3)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.enqueue(40)  # Should show that queue is full

q.dequeue()
q.display()

print("Is queue full?", q.is_full())
print("Is queue empty?", q.is_empty())
print("Current size:", q.size())
print("Front item (peek):", q.peek())
print("Final Queue contents:", q.display())
# 

