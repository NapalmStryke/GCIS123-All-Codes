#Implementing a Stack

class Node:
    __slots__ = ["__value", "__next"]
    def __init__(self, value, next = None):
        self.__value = value
        self.__next = next  
        
    def getValue(self):
        return self.__value

    def getNext(self):
        return self.__next

    def setNext(self, next):n
        self.__next = next
        
class Stacks: 
    __slots__ = ["__head", "__size"]
    def __init__(self):
        self.__head = Node("Head")
        self.__size = 0 #PUSH --> size + 1 and POP --> Size - 1
        
    def isEmpty(self):
        if self.__size == 0:
            return True
        return False

    def setSize(self, size):
        self.__size = size

    def getSize(self):
        return self.__size

    def push(self, value): #push monday
        node = Node(value) #node = Node("Monday")
        node.setNext(self.__head.getNext()) 
        self.__head.setNext(node)
        self.setSize(self.getSize() + 1)
        
    def peek(self):
        if self.isEmpty():
            print("Empty Stack!")
            return
        return self.__head.getNext().getValue()

    def pop(self):
        if self.isEmpty():
            print("Empty Stack!")
            return 
        removeTemp = self.__head.getNext()
        self.__head.setNext(self.__head.getNext().getNext())
        self.setSize(self.getSize() - 1)
        return removeTemp.getValue()
    
    def __repr__(self):
        current = self.__head.getNext()
        printstring = ""
        while current:
            printstring += str(current.getValue()) + ", "
            current = current.getNext()
        return printstring
    
    
def main():
    myWeek = Stacks()
    myWeek.setSize(0)
    myWeek.push("Monday")
    myWeek.push("Tuesday")
    myWeek.push("Wednesday")
    myWeek.push("Thursday")
    myWeek.push("Friday")
    myWeek.push("Saturday")
    myWeek.push("Sunday")
    print(myWeek.__repr__())
    myWeek.pop()
    print(myWeek.__repr__())
    
main()


