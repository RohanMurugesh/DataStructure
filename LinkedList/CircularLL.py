class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_in_empty(self, data):
        new_node = Node(data)
        new_node.next = new_node
        self.head = new_node

    def insert_at_beginning(self, data):
        if self.head is None:
            self.insert_in_empty(data)
            return
        new_node = Node(data)    # Create a new node
        temp = self.head     # Start from head #temp- temprovary variable
        while temp.next != self.head:  # Traverse to the last node
            temp = temp.next     # Move to the next node #temp.next- pointer to the next node
        temp.next = new_node      # Link last node to new node
        new_node.next = self.head   # Link new node to head
        self.head = new_node        # Update head to new node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_in_empty(data)
            return
        new_node = Node(data)
        temp = self.head
        while temp.next != self.head:   #Traverse to the last node
            temp = temp.next      # Traverse to the last node
        temp.next = new_node      # Link last node to new node
        new_node.next = self.head  # Link new node to head

    def insert_at_middle(self, data, position):
        if self.head is None:
            print("List is empty. Cannot insert at position", position)
            return
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)      # Create a new node
        temp = self.head           # Start from head
        count = 0                  # Initialize count
        
        while count < position and temp.next != self.head:   # Traverse to the position
            prev = temp                                      # Keep track of the previous node
            temp = temp.next                                 # Move to the next node
            count += 1                                       # Increment count

        if count != position:
            print(f"Position {position} out of range. Node inserted at end.")
            self.insert_at_end(data)
            return

        prev.next = new_node           # Link previous node to new node
        new_node.next = temp           # Link new node to current node
    
    def traverse(self):
        if self.head is None:
                print("List is empty")
                return
        temp = self.head
        while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:
                    break
        print("(back to head)")

# Delete at beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

# Delete at end
    def delete_at_end(self):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head

#Delete at middle
    def delete_at_middle(self, position):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        if self.head.next == self.head:
            self.head = None
            return
        if position == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        count = 0
        prev = None
        while count < position and temp.next != self.head:
            prev = temp
            temp = temp.next
            count += 1
        if count != position:
            print(f"Position {position} out of range. Cannot delete.")
            return
        prev.next = temp.next

# Function to print the list   
    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

# Example usage
cll = CircularLinkedList()

# Inserting in an empty list
cll.insert_in_empty(10)
print("After inserting in empty list:")
cll.print_list()

# Inserting at the beginning
cll.insert_at_beginning(5)
print("After inserting at beginning:")
cll.print_list()

# Inserting at the end
cll.insert_at_end(20)
print("After inserting at end:")
cll.print_list()

# Inserting at a specific position
cll.insert_at_middle(15, 1)  # Insert 15 at position 1
print("After inserting 15 at position 1:")
cll.print_list()

# Traversing the list
print("Traversing the list:")
cll.traverse()

# Original List after all the insertion operation
print("Original List:")
cll.print_list()

# Deleting at beginning
cll.delete_at_beginning()
print("After deleting at beginning:")
cll.print_list()

# Deleting at end
cll.delete_at_end()
print("After deleting at end:")
cll.print_list()

cll.insert_at_beginning(20)
cll.insert_at_end(30)
cll.print_list()

# Deleting at middle
cll.delete_at_middle(1)  # Delete node at position 1
print("After deleting at middle (position 1):") 
cll.print_list()


        

            
               



   