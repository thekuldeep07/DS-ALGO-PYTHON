class Node():
    def __init__(Self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleLinkedList():
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.length=0
    def append(self,data):
        newNode=Node(data)
        if self.head:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
            self.length+=1
        else:
            self.head=newNode
            self.tail=self.head
            self.length=1
    def prepend(self,data):
        newNode=Node(data)
        if self.head:
            self.head.prev=newNode
            newNode.next=self.head
            self.head=newNode
            self.length+=1
        else:
            self.head=newNode
            self.tail=self.head
            self.length=1
    def insert(self,data,index):
        newNode=Node(data)
        if index==0:
            self.prepend(data)
            return
        elif index >=self.length:
            self.append(data)
            return 
        else:
            temp=self.head
            i=0
            while i<self.length:
                if i < index-1:
                    nxt=temp.next
                    temp.next=newNode
                    newNode.prev=temp
                    newNode.next=nxt
                    nxt.prev=newNode
                    self.length+=1
                    return
                temp=temp.next
                i+=1
    def remove(self,index):
        i=0
        if index==0:
            self.head=self.head.next
            self.head.prev=None
            self.length-=1
            return
        elif index==self.length-1:
            self.tail=self.tail.prev
            self.tail.next=None
            selef.length-=1
            return
        else:
            temp=self.head
            while i <self.length:
                if i==index-1:
                    temp.next=temp.next.next 
                    temp.next.prev=temp
                    self.length-=1
                temp=temp.next
                i+=1
    def printDL(self):
        temp=self.head
        while temp!=None:
            print(temp.dat=a,end="->")
            temp=temp.next
        print()
        print(f"length = {self.length}")
            





            