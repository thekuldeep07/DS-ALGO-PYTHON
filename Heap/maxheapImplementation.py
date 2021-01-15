class MaxHeap:
    def __init__(self):
        self.heap=[ ]

    def get_parentIndex(self,i):
        if i > 0 :
             return (i-1)//2
        else:
            return -1     
    def get_leftChildIndex(self,i):
        return (2*i)+1
    def hasLeftChild(self,i):
        if self.get_leftChildIndex(i) < len(self.heap):
            return True
        else:
            return False

    def hasRightChild(self,i):
        if self.getRightChildIndex(i) < len(self.heap):
            return True
        else:
            return False


                
    def getRightChildIndex(self,i):
        return (2*i)+2
    def hasParent(self,i):
        return self.get_parentIndex(i)>=0

    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
       

    def insertKey(self,key):
        if len(self.heap)==0:
            self.heap.append(key)
            return      
        self.heap.append(key)
        self.heapifyUp(len(self.heap)-1)
        return

    def heapifyUp(self,i):
        size=len(self.heap)
        while self.hasParent(i) and (self.heap[self.get_parentIndex(i)] < self.heap[i]) :
             self.swap(i,self.get_parentIndex(i))
             i=self.get_parentIndex(i)
    def print1(self):
        print(self.heap)

    def deleteRoot(self):
        if len(self.heap)==0 :
            return -1
        lastIndex=len(self.heap)-1
        self.swap(0,lastIndex)
        root=self.heap.pop()
        self.heapifyDown(0)
        return root

    def heapifyDown(self,i):
        while(self.hasLeftChild(i)):
             maxChildIndex=self.getMaxChild(i)
             if maxChildIndex == -1 :
                 break
             if self.heap[i]<self.heap[maxChildIndex] :
                 self.swap(i,maxChildIndex)
             else:
                 break         


    def getMaxChild(self,i):
        if self.hasLeftChild(i):
            lc=self.get_leftChildIndex(i)
            if self.hasRightChild(i):
                rc=self.getRightChildIndex(i)
                if (self.heap[lc]> self.heap[rc]):
                    return lc
                else:
                    return rc
            else:        
                return lc 
        else:
            return -1               
                








heap1 = MaxHeap()
heap1.insertKey(8)
heap1.insertKey(7)
heap1.insertKey(6)
heap1.insertKey(9)
heap1.insertKey(5)
heap1.insertKey(10)
heap1.print1()
heap1.deleteRoot()
heap1.print1()




