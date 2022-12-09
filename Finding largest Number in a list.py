a = []
n = int(input("Enter number of elements : "))
for i in range (0,n):
    b = int(input("Enter element : "))
    a.append(b)
a.sort()
print("Largest element is", a[n-1])

        
