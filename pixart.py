import turtle
import pixart

Pixel_Size = 15

def initialisation():
    turtle.speed(0)
    turtle.tracer(False)
    turtle.up()
    turtle.goto(-300, -300)
    turtle.pencolor("black")
    turtle.fillcolor("pink")
    turtle.pensize(1)
    
def draw():
    i = 0
    turtle.begin_fill()
    turtle.down()
    while (i < 4):
        turtle.forward(Pixel_Size)
        turtle.right(90)
        i += 1
    turtle.up()
    turtle.end_fill()
    turtle.forward(Pixel_Size)
    
    
def pixart_move(row, col):
    xcor = -300
    ycor = 300
    turtle.goto(xcor, ycor)
    xcor += Pixel_Size * col
    ycor += ycor + Pixel_Size * row
    turtle.goto(xcor, ycor)
    
def draw_row(number_pixels):
    for i in range(20):
        turtle.penup()
        turtle.goto(0, Pixel_Size*i)
        turtle.pendown()
        
        for x in range(number_pixels):
            if (x + i) % 2 == 0:
                color = "black"
            else:
                color = "red"
            turtle.fillcolor(color)
            draw()
    

 

def main():
    initialisation()
    draw_row(20)
    input("END: ")
    
main()