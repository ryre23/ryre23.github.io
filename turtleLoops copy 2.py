import turtle


martin = turtle.Turtle()
screen = turtle.Screen()



#[inclusive,exclusive]

#angle formula = [(n-2) * 280]/number of sides (--and then--)  180 - answer



for i in range(4):
    martin.forward(90)
    martin.right(90)

for i in range(3):
    martin.forward(90)
    martin.left(120)
    
for i in ["lightBlue" , "darkBlue" , "blue"]:
    martin.color(i)
    martin.forward(90)
    martin.left(120)

numSides = input("How many sides? ")
nums = int(numSides)
insideVal = (nums-2) * 180 / nums
angleVal = 180 - insideVal

for i in range(nums):
    martin.forward(1)
    martin.right(angleVal)
    



    
