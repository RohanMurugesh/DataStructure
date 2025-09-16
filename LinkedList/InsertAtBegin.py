class Node:                           
    def __init__(self, data):
        self.data = data
        self.next = None
head = None                   #Initialize head as None, starts with empty list
#function to insert a new node at the beginning
def insert_at_begin(head,data):
    new_node = Node(data)     #create a new node
    new_node.next = head      #points new node to current head
    head = new_node     #update head to new node
    return head #update head to new node
#function to print the linked list
def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

#Example usage
head = insert_at_begin(head, 10)    #Insert 10 at the beginning
head = insert_at_begin(head, 20)    #Insert 20 at the beginning        
head = insert_at_begin(head, 30)    #Insert 30 at the beginning
display(head)   #Display the linked list