def MergeSort(arr):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2] #  [2,6,1,3]
        rightArr = arr[len(arr)//2:] # [5,7,8,4]
        MergeSort(leftArr) #1> [2,6] [1,3] 2> [2][6] [1][3] 3> [2] [6] [1] [3]
        MergeSort(rightArr)#1> [5,7] [8,4] 2> [5][7] [8][4] 3> [5] [7] [8] [4]
        i = j = k = 0
        while (i < len(leftArr)) and (j < len(rightArr)):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1
        #LEFTOVER ELEMENTS from left
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
        #LEFTOVER ELEMENTS from right 
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1
    print(arr)
            
def main():
    myArray = [2,6,1,3,5,7,8,4]
    MergeSort(myArray)
    
main()              

        
        