num = int(input("Enter num: "))

def FizzBuzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "Fizz"
    if num % 3 == 0:
        return "Buzz"
    return num

print (FizzBuzz(num))
