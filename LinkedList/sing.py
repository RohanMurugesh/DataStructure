class Node :
    def __init__(self,data):
        self.data= data
        self.next = None

class SinglyLinkedList :
    def __init__(self):
        self.head = None

    def insert_at_begin (self,data) :
        new_node = Node (data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end (self,data) :
        new_node = Node (data)
        if self.head is None :
            self.head = new_node
        else :
            temp = self.head
            while temp.next is not None :
                temp = temp.next
            temp.next = new_node

    def insert_at_index (self,target_value,data) :
        temp = self.head
        while temp is not None :
            if temp.data == target_value :
                new_node = Node (data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print (f"value {target_value} not found")                
                
    def delete_at_begin (self) :
        if self.head is None :
            print ("List is empty")
            return 
        self.head = self.head.next

    def delete_at_end (self) :
        if self.head is None :
            print ("List is empty")
            return 
        if self.head.next is None :
            self.head=None
            return
        temp=self.head
        while temp.next.next is None :
            temp = temp.next
            temp.next = None

    def delete_at_index (self,position) :
        if self.head is None:
            print ("List is empty")
            return
        if self.head.next is None :
            self.head = None
            return
        if position == 0 :
            self.head = self.head.next
            return 
        
        temp=self.head
        count = 0

        while temp.next is None and count < position-1 :
            temp = temp.next
            count +=1

        if temp is None :
            print ("Out of range")
            return
        
        temp.next = temp.next.next

    def print_list(self) :
        temp = self.head
    
        while temp is not None :
            print ( temp.data, end=" ->")
            temp = temp.next 

        print (None)


sl = SinglyLinkedList()

sl.insert_at_begin(10)
sl.insert_at_begin(20)
sl.insert_at_begin(30)

sl.print_list()

sl.insert_at_end(40)
sl.print_list()

sl.delete_at_begin()
sl.print_list()
sl.insert_at_index(10,25)
sl.print_list()


                   
                   




