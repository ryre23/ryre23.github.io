def addTwoNumbers(number1, number2):
    result = number1 + number2
    return result

def tipCalculator(subtotal, taxPerc, tipPerc):
    total = subtotal * taxPerc + subtotal
    tip = total * tipPerc
    print("The tip is " +str(tip))
    finalTotal = total + tip
    return finalTotal

#parameter or argument
#->are the things that go in the paranthesis

#return types
#the return type for input is a string
#whitespace- space that is white

answer=addTwoNumbers(111, 222)
print(answer)
answer2=addTwoNumbers(8439802,423890)
print(answer2)
answer3=tipCalculator(18.5, .075,.02)

def pythagorean(a, b):
    asquared = a**2
    bsquared = b**2
    summed = asquared + bsquared
    c = summed ** .5
    return c

c = pythagorean(3, 4)
print("c is " + str(c))

def compoundInterest(p, r, n, t):
    firstStep = r/n
    exponent = n * t
    secondStep = 1 + firstStep
    thirdStep = secondStep ** exponent
    fourthStep = p * thirdStep
    return fourthStep

a = compoundInterest(100, .01, 1, 1)
print("The interest is " + str(a))



