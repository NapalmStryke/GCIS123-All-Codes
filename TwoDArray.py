"""Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note : i = 0,1.., m-1 j = 0,1, n-1."""

def twoDeeArray(m,n):
    myArray = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        for j in range(n):
            myArray[i][j] = i*j 
    
    for row in myArray:
        for col in row:
            print(col,end = " ")
        print()

def main():
    first_digit = int(input("Enter first digit: "))
    second_digit = int(input("Enter second digit: "))
    twoDeeArray(first_digit, second_digit)
main()

