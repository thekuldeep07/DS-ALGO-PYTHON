from collections import deque

class Stack():
    def __init__(self):
        self.q1=deque()
        self.q2=deque()

    def push(self,data):
        while len(self.q1):
            self.q2.append(self.q1.popleft())
        self.q1.append(data)
        while len(self.q2):
            self.q1.append(self.q2.popleft())
    def pop(self):
        if not self.q1:
            return ("UNdereflow")
        else:
            return self.q1.popleft()            


s1=Stack()
s1.push(5)
s1.push(2)
print(s1.pop())
print(s1.pop())

