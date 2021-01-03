def bubbleSort(arr):
    n=len(arr)
    if n<=1:
        return
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

def optimizeBubblesort(arr):
    n=len(arr)
     n=len(arr)
    if n<=1:
        return
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                swapped=True
                arr[j],arr[j+1]=arr[j+1],arr[j]  
            if swapped == False:
                break      



arr=[5,3,0,144]
bubbleSort(arr)
print(arr)