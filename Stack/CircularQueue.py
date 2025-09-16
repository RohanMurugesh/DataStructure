class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size   
        self.front=self.rear=-1

    def is_empty(self):
        return self.front==-1

    def is_full(self):
        return (self.rear+1)%self.size==self.front
    
    def enqueue(self,item):
        if self.is_full():
            print("Queue is full")
            return
        if self.front==-1:  # 
            self.front=0
        self.rear=(self.rear+1)%self.size  # 
        self.queue[self.rear]=item  #
        print(f"Enqueued {item} to queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item=self.queue[self.front]
        if self.front==self.rear:  # 
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size  # 
        print(f"Dequeued {item} from queue")
        return item
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return []
        elements=[]
        i=self.front
        while True:
            elements.append(self.queue[i])
            if i==self.rear:
                break
            i=(i+1)%self.size
        return elements
    
cq=CircularQueue(3)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()

cq.dequeue()
cq.display()