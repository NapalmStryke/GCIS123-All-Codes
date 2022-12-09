class pizza:
    def __init__(self,CheeseTops,MeatTops,VegTops,Price): 
        self.__CheeseTops = CheeseTops #Private attribute which knows cheese topping of the pizza#
        self.__MeatTops = MeatTops #Private attribute which knows meat topping of the pizza# 
        self.__VegTops = VegTops #Private attribute which knows vegetable topping on the pizza#
        self.__Price = Price #Private attribute which knows total price of the pizza#
    
    ##AS THE ATTRIBUTES OF OUR CLASS ARE PRIVATE##
    ##WE HAVE MADE GETTER METHODS TO ACCESS THESE IF NEED TO##
    def getCheeseTops(self):
        return self.__CheeseTops
    def getMeatTops(self):
        return self.__MeatTops
    def getVegTops(self):
        return self.__VegTops
    def getPrice(self):
        return self.__Price
    def getPizzaDetails(self): #This getter gets all the details of the pizza including all toppings and total price#
        all = self.__CheeseTops + "," + "" + self.__MeatTops + "," + "" + self.__VegTops + "," + "$" + str(self.__Price)
        return all 
    
    ##AS THE ATTRIBUTES OF OUR CLASS ARE PRIVATE##
    ##WE MADE SETTER METHODS TO SET ANYTHING MANUALLY IF WE NEED TO##
    def setCheeseTops(self,CheeseTops):
        self.__CheeseTops = CheeseTops
    def setMeatTops(self,MeatTops):
        self.__MeatTops = MeatTops
    def setVegTops(self,VegTops):
        self.__VegTops = VegTops
    

