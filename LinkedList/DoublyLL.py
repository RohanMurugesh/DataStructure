class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        new_node.next = self.head  # Link new node to the former head
        self.head.prev = new_node  # Link former head back to new node
        self.head = new_node       # Update head to new node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return       #return after inserting the first node
        temp = self.head          
        while temp.next is not None:  # Traverse to the last node
            temp = temp.next  # Move to the next node
        temp.next = new_node  # Link last node to new node
        new_node.prev = temp  # Link new node back to last node

# For displaying the doubly linked list
    def forward_traversal(self):
      if self.head is None:
          print("List is empty")
          return
      temp = self.head
      while temp is not None:
          print(temp.data)
          temp = temp.next

# For backward traversal
    def backward_traversal(self):
      if self.head is None:
          print("List is empty")
          return
      temp = self.head
      while temp.next is not None:  # Traverse to the last node
          temp = temp.next
      while temp is not None:  # Traverse backward from the last node
          print(temp.data)
          temp = temp.prev

    # Insert at a specific index (0-based)
    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        count = 0
        while temp is not None and count < index - 1:
            temp = temp.next
            count += 1
        if temp is None:
            print("Index out of range.")
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node

#Delete at beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        if self.head.next is None:  # If there's only one node
            self.head = None      
            return                   #return after deleting the only node
        self.head = self.head.next  # Move head to the next node
        if self.head is not None:  # If the list is not empty after deletion
            self.head.prev = None   # Delete the previous link of the new head
            
#delete at end
    def delete_at_end(self):
        if self.head is None:  # If the list is empty
            print("List is empty. Cannot delete.")
            return  
        if self.head.next is None:  # If there's only one node
            self.head = None      
            return                 #return after deleting the only node
        temp = self.head         # Traverse to the last node
        while temp.next is not None:   # Move to the last node
            temp = temp.next    # Unlink the last node
        if temp.prev is not None:  # If there's a previous node
            temp.prev.next = None  # Unlink the last node from the second last node
        temp.prev = None          # Unlink the previous link of the last node

# Delete at middle
    def delete_at_middle(self,position):
        if self.head is None:  # If the list is empty
            print("List is empty. Cannot delete.")
            return
        if self.head.next is None:  # If there's only one node
            self.head = None
            return                   #return after deleting the only node
        if position == 0:
            self.head = self.head.next  
            if self.head is not None:
                self.head.prev = None
            return
        temp = self.head
        count = 0
        while temp is not None and count < position:
            temp = temp.next
            count += 1
        if temp is None:
            print("Position out of range.")
            return
        if temp.prev is not None:  # point previous node to next node
            temp.prev.next = temp.next  # Unlink the node to be deleted
        if temp.next is not None:     # point next node to previous node
            temp.next.prev = temp.prev   # Unlink the node to be deleted

# search for a value
    def search(self, key):            
        if self.head is None:
            print("List is empty")
            return
        temp = self.head           # Start from the head
        index = 0                   # Initialize index
         # Traverse the list
        while temp is not None:         # While there are nodes to check
            if temp.data == key:        # If the key is found
                print(f"Value {key} found at index {index}")
                return
            temp = temp.next        # Move to the next node
            index += 1          # Increment index

def display(head):    # head of the doubly linked list
    current = head    # Start from the head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")

# Example usage
dll = DoublyLinkedList()   # Create a new doubly linked list
#Insert nodes at the beginning
dll.insert_at_beginning(10) #Insert 10 at the beginning
dll.insert_at_beginning(20) #Insert 20 at the beginning
dll.insert_at_beginning(30) #Insert 30 at the beginning
display(dll.head)  # 30 <-> 20 <-> 10 <-> None
     
#Insert nodes at the end
dll.insert_at_end(40) #Insert 40 at the end 
display(dll.head)  # 30 <-> 20 <-> 10 <-> 40 <-> None

 # Forward traversal of the doubly linked list
dll.forward_traversal() #30 <-> 20 <-> 10 <-> 40 <-> None

# Backward traversal of the doubly linked list
dll.backward_traversal()  #40 <-> 10 <-> 20 <-> 30 <-> None

#Insert at specific index
dll.insert_at_index(2, 25) #Insert 25 at index 2
display(dll.head)  # 30 <-> 20 <-> 25 <-> 10 <-> 40 <-> None

#delete at beginning
dll.delete_at_beginning() #Delete node at the beginning
display(dll.head)  # 20 <-> 25 <-> 10 <->40 <-> None

#delete at end
dll.delete_at_end() #Delete node at the end
display(dll.head)  # 20 <-> 25 <-> 10 <-> None

#delete at middle
dll.delete_at_middle(1) #Delete node at index 1
display(dll.head)  # 20 <-> 10 <-> None

#search for a value
dll.search(10) #Value 10 found at index 1   
 