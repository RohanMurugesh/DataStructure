class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Dequeue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.front is None

    def addFront(self, item):
        new_node = Node(item)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def addRear(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def removeFront(self):
        if self.isEmpty():
            return None 
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return data

    def removeRear(self):
        if self.isEmpty():
            return None 
        data = self.rear.data
        if self.rear == self.front:
            self.rear = self.front = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return data

    def len(self):
        return self.size

    def display(self):
        current = self.front
        result = []
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

if __name__ == "__main__":
    dq = Dequeue()

    dq.addRear(1)
    dq.addRear(2)
    dq.addFront(3)

    print("Dequeue contents:", dq.display())  # Output: [3, 1, 2]

    print("Removed from front:", dq.removeFront())  # Output: 3
    print("After removing front:", dq.display())    # Output: [1, 2]

    print("Removed from rear:", dq.removeRear())    # Output: 2
    print("After removing rear:", dq.display())     # Output: [1]

    print("Is empty?", dq.isEmpty())                # Output: False
    print("Size:", dq.len())                       # Output: 1
