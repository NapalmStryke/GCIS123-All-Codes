#Bubble Sort

def BubbleSort(array): #TWO FOR LOOPS
    for j in range(len(array) - 1): #length  = 7 , last index = 6 #outside loop
        for i in range(len(array) - 1):  #inside loop 
            if array[i] > array[i + 1]: # is 44 greater than 10
                temp = array[i + 1] # temp = 10 
                array[i + 1] = array[i] # [44, 44, .......]
                array[i] = temp # [10, 44, ........]
    return array

def main():
    print(BubbleSort([44,10,12,100,-1,1,0]))
main()
            
            
# 5, 4, 3, 2, 1
# temp = 