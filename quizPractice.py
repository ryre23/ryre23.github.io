#General Format:
#def functionName(optionalParameters):
    #write code
    #return something

#def myster(string):

def grabLetter(word, index):
    letter = word[index]
    return letter

def firstHalf(string):
    midPoint = len(string) // 2
    firstHalf = string[0:midPoint]
    return firstHalf

def secondHalf(str):
    midPoint = len(str) // 2
    secondHalf = str[midPoint: len(str)]
    return secondHalf

def swapHalves(string):
    first = firstHalf(string)
    last = secondHalf(string)
    return last + first

def sameFirstLast(word):
    firstTwo = word[0:2]
    lastTwo = word[len(word) - 2: len(word)]
    if firstTwo == lastTwo:
        return True
    else:
        return False

print (swapHalves("Pizza"))

print (sameFirstLast("ZabeeZa"))

seggsy = "yessir"
print (seggsy[0:4:2])
