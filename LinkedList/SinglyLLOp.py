# Node class to represent each element in the list
class Node:
    def __init__(self, data):  #self-instance of a class, #initialiasion- Constructor method
        self.data = data  # Store data #data-parameter
        self.next = None  # Pointer to the next node

# Singly Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)     # Create a new node
        new_node.next = self.head # Point to the current head
        self.head = new_node      # Make new node the head

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If list is empty, new node is head
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next  # Move to the last node
            temp.next = new_node  # Add the new node at the end

    # Insert after a node with given value
    def insert_after_value(self, target_value, data):
        temp = self.head
        while temp is not None:
            if temp.data == target_value:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print(f"Value {target_value} not found in the list.")

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
        self.head = self.head.next

    #Delete at end
    def delete_at_end(self):
        if self.head is None:  # If the list is empty
            print("List is empty. Cannot delete.")
            return
        if self.head.next is None:  # If there's only one node
            self.head = None      
            return                   #return after deleting the only node
        temp = self.head         # Traverse to the second last node
        while temp.next.next is not None:   # Move to the second last node
            temp = temp.next    # Move to the next node
        temp.next = None    # Remove the last node

# Delete at middle
    def delete_at_middle(self,position):
        if self.head is None:  # If the list is empty
            print("List is empty. Cannot delete.")
            return
        if self.head.next is None:  # If there's only one node
            self.head = None
            return                   #return after deleting the only node
        
        if position == 0:  # If the position is 0, delete the head
            self.head = self.head.next  
            return
        
        temp = self.head
        count = 0
        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None :
            print("Position out of range.")
            return
        
        temp.next = temp.next.next
         
         
    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage
ll = LinkedList()

# Insert at beginning
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.print_list()  # 20 -> 10 -> None

# Insert at end
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.print_list()  # 20 -> 10 -> 30 -> 40 -> None

# Insert after a value
ll.insert_after_value(10, 25)
ll.print_list()  # 20 -> 10 -> 25 -> 30 -> 40 -> None

# Insert at a specific index
ll.insert_at_index(2, 15)
ll.print_list()  # 20 -> 10 -> 15 -> 25 -> 30 -> 40 -> None

# Delete at beginning
ll.delete_at_beginning()
ll.print_list()  # 10 -> 15 -> 25 -> 30 -> 40 -> None

# Delete at end
ll.delete_at_end()
ll.print_list()  # 10 -> 15 -> 25 -> 30 -> None

# Delete at middle
ll.delete_at_middle(2)  # Delete node at index 2
ll.print_list()  # 10 -> 15 -> 30 -> None

