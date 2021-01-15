class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack():
    def __init__(self):
        self.top=Node(None)
        self.bottom=Node(None)
        self.size=0

    def peek(self):
        if self.size==0:
            return "underflow"
        else:
            return self.top.data
    def push(self,data):
        newNode=Node(None)
        if self.bottom ==None:
            self.bottom=newNode
            self.top=self.bottom
            self.length+=1
        else:
            curr=self.top
            self.top=newNode
            self.top.next=curr
            self.length+=1

    def pop(self):
        if not self.top:
            return None
        poppedValue=self.top
        self.top=self.top.next
        return poppedValue

    def printStack(self):
        temp=self.top
        while temp!=None:
            print(temp.data,end='->')
            temp=temp.next
        print()    

