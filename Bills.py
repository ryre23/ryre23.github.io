def getNumberBills(change, typeOfBill):
    numberOfBills = change // typeOfBill
    return numberOfBills

amount = 18.76
num10s = getNumberBills(amount, 10)

print (num10s)

amount = amount - num10s * 10
num5s = getNumberBills(amount, 5)
print (num5s)

amount = amount - num5s * 5
num1s = getNumberBills(amount, 1)
print (num1s)

#.87 -> 3 quarters


def getNumberCoins(change, typeOfCoin):
    numberOfCoins = change // typeOfCoin
    return numberOfCoins


amount = .87

numQs = getNumberCoins(amount, .25)
print(numQs)
amount = amount - (numQs * 0.25)

numDs = getNumberCoins(amount, .10)
print(numDs)

amount = amount - (numDs * .10)

numNs = getNumberCoins(amount, .05)
print (numNs)
amount = amount - (numNs * .05)

numPs = getNumberCoins(amount, .01)
print (numPs)
