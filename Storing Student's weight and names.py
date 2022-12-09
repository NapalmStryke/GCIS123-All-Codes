weight = [ ]
name = [ ]
for counter in range (1,3):
    n = str(input("Enter student's name : "))
    if n in name:
        print ("Name is already in list")
        n = str(input("Please enter a different student's name : "))
        name.append(n)
    else:
        name.append(n)
    w = int(input("Enter student's weight : "))
    if w < 0 or w > 100:
        print("Invalid Weight")
        w = int(input("Please enter a valid weight : "))
        weight.append(w)
    else:
        weight.append(w)

while counter == max(counter):
    print (name[counter-1],"has a weight of ",weight[counter-1],"kg")
    print (name[counter-1],"has a weight of ",weight[counter-1],"kg")
    print (name[counter-1],"has a weight of ",weight[counter-1],"kg")
    print (name[counter-1],"has a weight of ",weight[counter-1],"kg")
    
            
