def QuickSort(array): #O(n) is the space complexity
    greater = []
    lesser = []
    if len(array) <= 1:
        return array
    else: 
        pivot = array[0]         
    for i in range(len(array)):
        if array[i] > pivot:
            greater.append(array[i])
        elif array[i] < pivot:
            lesser.append(array[i])
    return QuickSort(lesser) + [pivot] + QuickSort(greater)  
        
def main():
    array = []
    elements = int(input("How many elements in array: "))
    for i in range(elements):
        userInput = int(input("Enter element: "))
        array.append(userInput)
    print(QuickSort(array))
    
main()