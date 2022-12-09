import re
import csv

def zip_check(filename):
    with open(filename) as myFile:
        csv_reader = csv.reader(myFile)
        next(csv_reader)
        for tokens in csv_reader:
            if re.findall("[7,8,9][0-9]{4}",tokens[2]):
                print("Found a Match:",tokens[2])
            else:
                print("No match found!")
                
def guessingName():
    number = int(input("Enter a number: "))
    if (number < 1 or number > 10):
        raise ValueError("The guess is wrong...")
    print("You picked:", number)
          
      
        
def main():
    zip_check("zipcodes.csv")
    guessingName()
    
if __name__ == "__main__":    
    main()