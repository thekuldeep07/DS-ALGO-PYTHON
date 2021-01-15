class CircularQueue():
    def __init__(self,size):
        self.size=size
        self.queue=[None]*self.size
        self.front=self.rear=-1

    def enqueue(self,data):
        if self.front ==-1:
            self.front=self.rear=0
            self.queue[self.front]=data
        elif (self.rear+1)%self.size == self.front:
            print("queue is full")  
        else: 
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if self.front ==-1:
            print("Queue is empty")
        elif(self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        if self.front ==-1:
            return "underflow"
        elif self.rear>=self.front:
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end='->')
            print()    
        else:
            for i in range(self.front,self.size):
                print(self.queue[i],end='->')
            for i in range(0,self.rear+1):
                print(self.queue[i],end='->')  
            print()      



        
