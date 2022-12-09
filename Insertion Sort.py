#Insertion Sort
def InsertionSort(array):
    n = len(array)
    #0th index is already "sorted" incrementing starts from 1
    for i in range(1,n): 
        j = i - 1 #decrementing array comparing right to left
        temp = array[i]
        while j >= 0 and array[j] > temp: #j can't be less than 0
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp #case where the value finds it correct position
    return array

#asking for user input
numberList = []
num = int(input("How many elements: "))
for i in range(num):
    userInput = int(input("Enter number: "))
    numberList.append(userInput)
print(numberList)

print(InsertionSort(numberList))


        

    



