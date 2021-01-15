class Array():
    def __init__(self):
        self.data={}
        self.length=0
    def __str__(self):
        return str(self.__dict__)  

    def insert(self,item):
        self.data[self.length]=item
        self.length+=1
    def pop(self):
        lastItem=self.data[self.length-1]
        del self.data[self.length-1]  

        self.length-=1
        return lastItem
    def delete(self,index):
        deleteItem=self.data[index]
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]  
        del self.data[self.length-1]
        self.length-=1
        return deleteItem
arr = Array()
arr.insert(3)
print(arr)                
