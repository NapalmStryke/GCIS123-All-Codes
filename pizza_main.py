##This solution was implemented by Taha Naveed, Syed Ibrahim, Naylin Aung and AbdulRahman##
import toppingFile 
import pizzaFile
from toppingFile import toppings 
from pizzaFile import pizza



#These dictionaries are designed to help user with their topping choices and to reflect that emphasize to them that each topping is unique#

cheese_toppings = {'mz': 'Mozarella', 'sd': 'Standard', 'ch': 'Cheddar'}

meat_toppings = {'p': 'Pepporoni', 's': 'Sausage', 'b': 'Bacon'}

veg_toppings = {'n': 'None', 'j': 'Jalepenos', 'm': 'Mushrooms'}

def greetuser(): ##This function is created to greet a user when placing a new order, it gives all the basic info##
    print("--WELCOME TO TAHA'S PIZZA--")
    print("")
    print("DISCLAIMER : WE ONLY SELL PIZZAS IN PAIRS.")
    print("")
    print("THE BASE RATE IS $5")
    
def secondpizzaprompt():#This function is called when the user has chosen their first pizza succesfully##
    print("")
    print("")
    print("-NOW YOU WILL CHOOSE YOUR SECOND PIZZA WITH THE EXACT SAME OPTIONS-")
    print("-SECOND PIZZA CHOICE:  ")



    


    
    

    
    

    
    
    


##We have offered three types of topping varieties using three diffrent dictionaries##

def main():
    greetuser()

    ##THE PROCEDURE OF GETTING A CHEESE TOPPING FROM A USER##
    print("What type of cheese do you want ?")
    print("The additional prices are: ")
    print("Mozarella : $2", "Standard : $0", "Cheddar : $1" )
    print("")
    for i in cheese_toppings:
        print("ENTER CODE:","",i,"","FOR",cheese_toppings[i]) ##this loop prints the keys value pairs from dict for the user to make a choice##

    print("")
    user_code = input("Choose your cheese topping:") ##user prefrence noted
    if user_code in cheese_toppings: ##This conditional statement makes sure that the user's choice is valid
        print(f"Your choice is, {cheese_toppings[user_code]}")
        Topping_Name = cheese_toppings[user_code]
        
    else: 
        print("Your choice was invalid !, Run the program again !") #IF the user's choice is invalid, they must enter their choices again
        exit
    
    if Topping_Name == "Mozarella": #This conditional statement assigns prices based on the user's topping choice#
        user_price = 2 
    elif Topping_Name == "Standard":
        user_price = 0
    elif Topping_Name == "Cheddar":
        user_price = 1 
    
    user_cheese_topping = toppingFile.toppings(Topping_Name,user_code,user_price) #creating a topping object from the user's choice#
    val = user_cheese_topping.getDetails() #a method from the class called to give the user details of their choice 
    PriceTotal = user_cheese_topping.getPrice() #a method from the class called which helps us determine the price of this topping, we're keeping a running total in the variable PriceTotal#

    print("Details of your Cheese Toppings ! :", val)
    ##CHEESE TOPPINGS COLLECTED FROM USER##

    ##THE PROCEDURE OF GETTING MEAT TOPPINGS FROM A USER, pretty much the same procedure is used as the last topping##
    print("")
    print("What type of meat do you want ?")
    print("The additional prices are: ")
    print("Pepparoni : $2", "Sausage : $1", "Bacon : $3" )
    print("")
    for i in meat_toppings:
        print("ENTER CODE:","",i,"","FOR",meat_toppings[i])
    print("")
    user_code2 = input("Choose your meat topping:")
    if user_code2 in meat_toppings:
        print(f"Your choice is, {meat_toppings[user_code2]}")
        Topping_Name_2 = meat_toppings[user_code2]
    else: 
        print("Your choice was invalid !, Run the program again !")
        exit
    if Topping_Name_2 == "Pepporoni": 
        user_price_2 = 2
    elif Topping_Name_2 == "Sausage":
        user_price_2 = 1
    elif Topping_Name_2 == "Bacon":
        user_price_2 = 3
    
    user_meat_topping = toppingFile.toppings(Topping_Name_2,user_code2,user_price_2)
    val2 = user_meat_topping.getDetails()
    
    PriceTotal = PriceTotal + user_meat_topping.getPrice()
    print("Details of your meat toppings are:", val2)
    ##MEAT TOPPINGS COLLECTED FROM USER##

    ##VEGETABLE TOPPINGS COLLECTION PROCEDURE FROM USER, the same method is used##
    print("")
    print("What type of veggie toppings do you want ?")
    print("The additional prices are: ")
    print("None : $0", "Jalepeno : $1", "Mushrooms : $2")
    print("")
    for i in veg_toppings:
        print("ENTER CODE:","",i,"","FOR",veg_toppings[i])
    print("")

    user_code3 = input("Choose your veggie topping:")
    if user_code3 in veg_toppings:
        print(f"Your choice is, {veg_toppings[user_code3]}")
        Topping_Name_3 = veg_toppings[user_code3]
    else: 
        print("Your choice was invalid !, Run the program again !")
        exit
    
    if Topping_Name_3 == "None": 
        user_price_3 = 0
    elif Topping_Name_3 == "Jalepenos":
        user_price_3 = 1
    elif Topping_Name_3 == "Mushrooms":
        user_price_3 = 2

    user_veg_topping = toppingFile.toppings(Topping_Name_3,user_code3,user_price_3)
    val3 = user_veg_topping.getDetails()
    PriceTotal = PriceTotal + user_veg_topping.getPrice()
    print("Details of your veg toppings are:", val3)
    ##VEGETABLE COLLECTION PROCEDURE DONE##


    ##FINALIZING THE FIRST PIZZA##
    print("")
    print("")
    PriceTotal = PriceTotal + 5 #adding the base $5 to additional topping costs
    pizza_one = pizzaFile.pizza(Topping_Name,Topping_Name_2,Topping_Name_3,PriceTotal) #creating a pizza object from user's choices#

    pizzaInfo = pizza_one.getPizzaDetails()

    print("")

    print("YOUR FIRST PIZZA IS ---- ", pizzaInfo)
    secondpizzaprompt()
    ##FIRST PIZZA FINALIZED##

    #CHEESE TOPPING COLLECTION FOR SECOND PIZZA#
    print("What type of cheese do you want ?")
    print("The additional prices are: ")
    print("Mozarella : $2", "Standard : $0", "Cheddar : $1" )
    print("")
    for i in cheese_toppings:
        print("ENTER CODE:","",i,"","FOR",cheese_toppings[i]) ##this loop prints the keys value pairs from dict for the user to make a choice##

    print("")
    print("")
    user_code4 = input("Choose your cheese topping:") ##user prefrence noted
    if user_code4 in cheese_toppings: ##This conditional statement makes sure that the user's choice is valid
        print(f"Your choice is, {cheese_toppings[user_code4]}")
        Topping_Name4 = cheese_toppings[user_code4]
    else: 
        print("Your choice was invalid !, Run the program again !") #IF the user's choice is invalid, they must enter their choices again
        exit
    
    if Topping_Name4 == "Mozarella": #This conditional statement assigns prices based on the user's topping choice#
        user_price4 = 2 
    elif Topping_Name4 == "Standard":
        user_price4 = 0
    elif Topping_Name4 == "Cheddar":
        user_price4 = 1 
    user_cheese_topping2 = toppingFile.toppings(Topping_Name4,user_code4,user_price4)
    val4 = user_cheese_topping2.getDetails()
    PriceTotal_2 = user_cheese_topping2.getPrice() ##This running total is for the second pizza##
    print("Details of your Cheese Toppings ! :", val4)
    ##CHEESE TOPPING COLLECTED FOR SECOND PIZZA##

    ##MEAT TOPPING COLLECTION FOR SECOND PIZZA##
    print("")
    print("What type of meat do you want ?")
    print("The additional prices are: ")
    print("Pepparoni : $2", "Sausage : $1", "Bacon : $3" )
    print("")
    for i in meat_toppings:
        print("ENTER CODE:","",i,"","FOR",meat_toppings[i])
    print("")
    user_code5 = input("Choose your meat topping:")
    if user_code5 in meat_toppings:
        print(f"Your choice is, {meat_toppings[user_code5]}")
        Topping_Name_5 = meat_toppings[user_code5]
    else: 
        print("Your choice was invalid !, Run the program again !")
        exit
    if Topping_Name_5 == "Pepporoni": 
        user_price_5 = 2
    elif Topping_Name_5 == "Sausage":
        user_price_5 = 1
    elif Topping_Name_5 == "Bacon":
        user_price_5 = 3
    user_meat_topping2 = toppingFile.toppings(Topping_Name_5,user_code5,user_price_5)
    val5 = user_meat_topping2.getDetails()
    
    PriceTotal_2 = PriceTotal_2 + user_meat_topping2.getPrice()
    print("Details of your meat toppings are:", val5)
    ##MEAT TOPPING COLLECTED FOR SECOND PIZZA##

    ##VEGETABLE TOPPING COLLECTION FOR SECOND PIZZA##
    print("")
    print("What type of veggie toppings do you want ?")
    print("The additional prices are: ")
    print("None : $0", "Jalepeno : $1", "Mushrooms : $2")
    print("")
    for i in veg_toppings:
        print("ENTER CODE:","",i,"","FOR",veg_toppings[i])
    print("")

    user_code6 = input("Choose your veggie topping:")
    if user_code6 in veg_toppings:
        print(f"Your choice is, {veg_toppings[user_code6]}")
        Topping_Name_6 = veg_toppings[user_code6]
    else: 
        print("Your choice was invalid !, Run the program again !")
        exit
    
    if Topping_Name_6 == "None": 
        user_price_6 = 0
    elif Topping_Name_6 == "Jalepenos":
        user_price_6 = 1
    elif Topping_Name_6 == "Mushrooms":
        user_price_6 = 2

    user_veg_topping2 = toppingFile.toppings(Topping_Name_6,user_code6,user_price_6)
    val6 = user_veg_topping2.getDetails()
    PriceTotal_2 = PriceTotal_2 + user_veg_topping2.getPrice()
    print("Details of your veg toppings are:", val6)
    ##VEGETABLE TOPPING COLLECTION FOR SECOND PIZZA DONE##

    ##FINALIZING SECOND PIZZA AND PRICE FOR USER##
    print("")
    print("")
    PriceTotal_2 = PriceTotal_2 + 5 #adding the base $5 to additional topping costs
    pizza_two = pizzaFile.pizza(Topping_Name4,Topping_Name_5,Topping_Name_6,PriceTotal_2) #creating a pizza object from user's choices#

    pizzaInfo_2 = pizza_two.getPizzaDetails()

    print("")
    print("")

    print("YOUR SECOND PIZZA IS ---- ", pizzaInfo_2)

    Sum = pizza_one.getPrice() + pizza_two.getPrice()
    print("")
    print("")
    print("YOUR TOTAL BILL WAS : ---$", Sum)
    
    

main()

