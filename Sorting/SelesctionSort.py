def selectionSort(arr):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

#below is the stable selection sort using insettion instead of swapping
def stableSelctionSort(arr):
    for i in range(n):
        min =i
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                min=j
        key=arr[min]        
        while min >i:
            arr[min]=arr[min-1]
            min-=1
        arr[i]=key    


