# Nay Lin
END = 0
array = [33,42,23,56,99,69,21,42,12,4]
search = int(input("Enter a number to search : "))

for i in range(len(array)):
    if search == array[i]:
        print("Found at index",i)
        break
if search not in array: 
    print("Not Found.")
