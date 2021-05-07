import turtle

sandbox = turtle.Screen()

martin = turtle.Turtle()

#conditional statements
#for us to make decisions

#boolean -> new data type (like int, float, str)
#it can only be True or False

holder = True
print(holder)

#operators to create booleans
# > < >= <= == !=

greater7 = 9 > 7
print(greater7)

equalto7 = 9 == 7
# = the assignment operator

number = 7
print(equalto7)

number = 7
number = 0

if number > 0:
    print("Positive")
elif number == 0:
    print("Zero!")
else:
    print("Negative")


print("DONE") 

for i in range(1800):
    martinColor = input("What color do you want?")
    direction = input("What direction do you want to turn?")
    degrees = input("How many degrees do you want to turn?")
    degrees = int(degrees)

    distance = input("How far do you want to travel?")
    distance = int(distance)

    pen = input("Would you like the pen down?")

    martin.color(martinColor)
    
    if direction == "right" and degrees <= 180:
        martin.right(degrees)
    elif direction == "right" and degrees > 180:
        martin.left(360 - degrees)
    elif direction == "left" and degrees <= 180:
        martin.left(degrees)
    else:
        martin.right(360 - degrees)
    

    if pen == "yes":
        martin.pendown()
    else:
        martin.penup()

    martin.forward (distance)
