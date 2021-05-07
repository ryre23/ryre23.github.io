print ("Hello, World!")
print (2 + 2)
print (18 % 3)

#variables
#variables are a way for us to store data/information

myName = "Ryan Reiss"
print (myName)

numbers = 2 + 2
print (numbers)

tricky = "2 + 2"
print (tricky)


subtotal = 19.78
taxRate = 0.075
tipPercentage = 0.28

tax = subtotal * taxRate
total = tax + subtotal
tipAmount = total * tipPercentage

print ("The tip is: " + str(tipAmount))

#Concatenate - >> means glue two strings together

#String -> text
#Float -> decimal numbers
#Integer -> whole numbers

finalTotal = total + tipAmount
print ("The final total is: " + str(finalTotal))

