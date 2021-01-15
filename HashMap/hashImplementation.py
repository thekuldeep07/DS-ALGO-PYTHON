class MyHashMap():
    def __init__(self):
        self.size=50
        self.map=[None]*self.size
    def getHash(self,key):
        h=0
        for c in str(key):
            h+=ord(c)
        return h %self.size
    def set(self,key,value):
        address=self.getHash(key)
        if self.map[address]==None:
            self.map[address]=[]
        self.map[address].append([key,value])
    def get(self,key):
        address=self.getHash(key)
        bucket=self.map[address]
        if bucket:
            for i in range (len(bucket)):
                if bucket[i][0]== key:
                    return bucket[i][1]
        else:
            return "undefined"

map1=MyHashMap()
map1.set('hii',101)
print(map1.get('hii'))

