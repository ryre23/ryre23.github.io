#Iteration

##for i in range (0,4):
## timmy.forward(100)
## timmy.right(90)

for i in range(0, 10, 2):
    print(i)

print("------")
word = "empanada"

for index in range (0, len(word)):
    print(word[index])

print("------")

for index in range (0, len(word) // 2):
    print(word[index])


print("------")


for index in range (len(word) // 2, len(word)):
    print(word[index])
 
#aggregation -> a fancy collection

basket = 0
word = "abchiabchello"
for index in range(0, len(word)):
    egg = word[index]
    if egg == "abc":
        basket = basket + 1
print (basket)

#counting abc's
abcBasket = 0
for index in range(0, len(word)):
    stoppingPoint = index + 3
    window = word[index : stoppingPoint]
    if window == "abc":
        abcBasket = abcBasket + 1

print (abcBasket)


def containsE(word):
    for index in range(0, len(word)):
        letter = word[index]
        if letter == "e":
            return True
    #outside of loop
    return False

def containsHello(yellow):
    #looking for hello
    for index in range(0, len(yellow)):
        stoppingPoint = index + 5
        window = yellow[index: stoppingPoint]
        if window == "hello":
            return True
    return False

print (containsHello("abchelloxyz"))
print (containsHello("abcxyz"))


def aNoZ(phrase):
    flag = False
    for index in range(0, len(phrase)):
        letter = phrase[index]
        if letter == "a":
            flag = True
        if letter == "z":
            return False;
    if flag == True:
        return True
    else:
        return False


def isPalindrome(phrase):
    backwards = " "
    for index in range (len(phrase) -1, -1, -1):
        letter = phrase[index]
        backwards = backwards + letter
    if backwards == phrase:
        return True
    else:
        return False
    


