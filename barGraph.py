import turtle
sandbox = turtle.Screen()
chad = turtle.Turtle()


data = "2387419"

def drawBar(height, width, color):
    chad.begin_fill()
    for i in range(0, 4):
        chad.color(color)
        if i == 0 or i == 2:
            chad.forward(width) 
        else:
            chad.forward(height)
        chad.left(90)
    chad.end_fill()
    chad.forward(20)
    chad.penup()
    chad.forward(20)
    chad.pendown()

drawBar(70, 20, "green")
drawBar(140, 20, "crimson")
        
