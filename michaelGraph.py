import turtle

sandbox = turtle.Screen()
fred = turtle.Turtle()

#creating an xy-plane through turtlea

#fred.forward(90)
#fred.left(90)
#fred.forward(90)
#fred.left(180)
#fred.forward(90)
#fred.left(90)
#fred.forward(90)
#fred.left(180)
#fred.forward(90)
#fred.left(90)
#fred.forward(90)


for _ in range(4):
    position = fred.position()
    fred.forward(90)
    fred.setposition(position)
    fred.right(90)
    
