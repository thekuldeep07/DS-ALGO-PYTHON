class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.length=0
        self.head=Node(None)
        self.tail=Node(None)

    def append(self,data):
        newNode=Node(data)
        if self.head:
            self.tail.next=newNode
            self.tail=newNode
        else:
            self.head=newNode
            self.tail=newNode
        self.length+=1

    def prepend(self,data):
        newNode=Node(data)
        if self.head:
            newNode.next=self.head
            self.head=newNode
        else:
            self.head=newNode
            self.tail=self.head
        self.length+=1


    def insert(self,data,index):
        newNode=Node(data)
        i=0
        temp=self.head
        if index ==0:
            self.prepend(data)
            return
        elif index >=self.length:
            self.append(data)
            return
        else:
            while i<self.length:
                if i==index-1:
                    temp.next=newNode
                    newNode.next=temp.next
                    self.length+=1
                    break
                temp=temp.next
                i+=1

    def printLL(self):
        temp=self.head
        while temp != None:
            print(temp.data,end="->")
            temp=temp.next
        print()
        print(f"length = {self.length}")

    def remove(self,index):
        temp=self.head
        i=0
        if index ==0:
            self.head=self.head.next
            self.length-=1
            return    
        elif index > self.length:
            return "enetered wrong index"
        else:
            while i<self.length:
                if i=index-1:
                    temp.next=temp.next.next
                    self.length-=1
                    return
                i+=1
                temp=temp.next
    def reverse(self):
        curr=self.head
        prev = None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev                
                


                    





            
