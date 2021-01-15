from collections import deque
class Stack():
    def __init__(self):
        self.q1=deque()
    def push(self,data):
        self.q1.append(data)
    def reverse(self):
        if not self.q1:
            return
        front=self.q1.popleft()
        self.reverse()
        self.q1.append(front)
    def pop(self):
        if not self.q1:
            return "Underflow"
        self.reverse()
        front=self.q1.popleft()
        self.reverse()
        return front
s1=Stack()
s1.push(5)
s1.push(2)
print(s1.pop())        
 
