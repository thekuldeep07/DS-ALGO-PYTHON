def heapifyDown(arr,n,i):
    largest=i
    l=2*i + 1
    r=2*i+ 2
    if l < n and arr[l] > arr[i]:
        largest=l
    if r < n and arr[r]> arr[largest]:
        largest=r 
    if largest !=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapifyDown(arr,n,largest)
def HeapSort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapifyDown(arr,n,i)   
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapifyDown(arr,i,0)        


arr=[5,7,2,9,7,6,0]
HeapSort(arr)
print(arr)

