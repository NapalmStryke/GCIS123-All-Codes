x = ()
def fun(z,y=2):
    return z*y
x = int(input("Enter a number : "))
p = fun(x)
print ("Double of your number is :",p)

ans = str(input("Would you like to square your number ? : "))

if ans == ("yes"):
    p = p**2
    print("The square of your number is : ",p)
elif ans == ("no"):
    print("GOODBYE")
else:
    x = int(input("Enter a number : "))
    p = fun(x)
    print ("Double of yoiur number is :",p)


