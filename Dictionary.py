def names():
    myDict = {}
    myDict["N"] = ["Nay", "Lin", "Myanmar"]
    myDict["T"] = ["Taha", "Naveed", "Pakistan"]
    myDict["A"] = ["Abdulrahman", "Ali", "Sudan"]
    myDict["S"] = ["Syed", "Ibrahim", "Pakistan"]
    for name in myDict:
        print(name, ":", myDict[name])
    

    
def main():
    names()
    
main()