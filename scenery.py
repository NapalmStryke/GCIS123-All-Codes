"""
GCIS_ACTIVITY_1; this project was done by Taha Naveed, Syed Ibrahim and Nay Lin Aung. We have used a larger canvas and the results are,
better visable in full screen
"""


import turtle 

base_1 = int(input("enter the base for your first house. NOTE: 250-300 is the ideal base: ")) ###the base of the first house is taken from the user to establish a constant height, ideal value is <= 300
height = base_1//2 ###height is now used as a global variable, it is the height of the rectangles


###this rectangle functions takes in 3 arguments and draws a colored rectangle###
def rectangle(height,width,bodycolor):
    
    start = turtle.pos()
    turtle.pendown()
    turtle.color(bodycolor)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(90)
    turtle.goto(start)
    turtle.end_fill()

###this function makes use of a rectangle and circle to draw trees 
def lollipop_tree(height,diameter):
    width = height//8 ##width is 1/8 of the height to make the tree thin###
    mid_width = width/2
    start = turtle.pos()
    turtle.color("Brown") ##the trunk is always kept brown##
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.forward(height)
    top = turtle.pos()
    turtle.setheading(360)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)
    turtle.goto(start)
    turtle.end_fill()
    turtle.goto(top)
    turtle.color("Green") ##the body (leaves) of the tree is always kept green##
    turtle.begin_fill()
    turtle.setheading(360)
    turtle.forward(mid_width)
    turtle.circle(diameter)
    turtle.end_fill()

    turtle.down()



###this function creates an isoceles triangle in the place of the roof, the rectnagle and triangle on top share the same base###
def roof(base,sides,roofcolor):
    base = int(base)
    base_sq = base**2
    base_sq = base_sq/4
    sides_sq = sides**2
    
    height_of_triangle = sides_sq - base_sq
    height_of_triangle = height_of_triangle**(1/2)
    
    

    
    start = turtle.pos()
    turtle.color(roofcolor)
    turtle.begin_fill()
    turtle.penup()
    turtle.forward(base/2)
    turtle.pendown()
    base_middle = turtle.pos()
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()

    turtle.pendown()
    turtle.forward(base) ###base drawn###

    endpoint_1 = turtle.pos()
    turtle.pendown()
    turtle.goto(base_middle)
    turtle.setheading(90)
    turtle.penup()
    
    turtle.forward(height_of_triangle)
    
    maximum = turtle.pos()
    turtle.pendown()
    turtle.goto(endpoint_1)####one side drawn
    turtle.end_fill()

    turtle.begin_fill()
    turtle.goto(maximum)
    turtle.goto(start) ###second side drawn
    turtle.end_fill()


def house_1(roofcolor,bodycolor):
    global height
    global base_1
    width = base_1
    area = height*base_1
    print("the area of the smaller facade on the right is:", area, "units")
    midpoint = height//2
    sides = base_1 + 50 
    
    roof(base_1,sides,roofcolor)

    turtle.setheading(360)
    

    rectangle(height,width,bodycolor)

    ##drawing the door of the house, suitable to its size. The global height variable is used again to find proportions##
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(height)
    turtle.setheading(360)
    turtle.forward(base_1//2)
    turtle.setheading(90)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.forward(height//3)
    turtle.setheading(360)
    turtle.forward(height//6)
    turtle.setheading(270)
    turtle.forward(height//3)
    turtle.setheading(180)
    turtle.forward(height//6)
    turtle.end_fill()

def house_2(base_2,roofcolor,bodycolor):
    global height
    width = base_2 ##base 2 is a local variable
    area = width*height
    print("the area of the bigger facade on the left is:", area, "units")
    midpoint = height//2
    sides = base_2 + 50

    roof(base_2,sides,roofcolor)
    turtle.setheading(360)
    rectangle(height,width,bodycolor)

    ###drawing the door of the second house
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(height)
    turtle.setheading(360)
    turtle.forward(base_2//2)
    turtle.setheading(90)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.forward(height//2)
    turtle.setheading(360)
    turtle.forward(height//4)
    turtle.setheading(270)
    turtle.forward(height//2)
    turtle.setheading(180)
    turtle.forward(height//4)
    turtle.end_fill()
    
   
def main():  
    global height
    global base_1
    house_1("Pink","Brown") 
    turtle.penup()
    
    
    turtle.goto(-400,0) ##the turtle goes 400 units to the left from origin to make space for the second house##
    turtle.setheading(360)
    turtle.pendown()
    
    house_2(350,"Red","Brown") ###keep the second base <= 350, it is the bigger house 
    turtle.penup()
    turtle.down()
    turtle.penup()
    turtle.goto(-600,0) ##the trees are drawn equal distances from the origin##
    turtle.setheading(270)
    turtle.forward(height)
    turtle.pendown()
    lollipop_tree(300,100)

    turtle.penup()
    turtle.goto(500,0)
    turtle.setheading(270)
    turtle.forward(height)
    turtle.pendown()
    lollipop_tree(300,100)
    input("stop.....")
    

    

main()
