def mergeSort(arr):
    if len(arr)>1:
        middle=(l+r)//2
        l=arr[:middle]
        r=arr[middle+1:r]
        mergeSort[l]
        mergeSort[r]
        i=j=k=0
        while i<len(l) and j< len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1 
            k+=1
        while i < len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1
            


        
        