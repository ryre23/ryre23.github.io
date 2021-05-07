def lastTwo(word):
    #lastletter = word[len(word)]
    #^ triggers index out of bounds
    lastLetter = word[len(word)-1]
    secondToLastLetter = word[len(word) - 2]

    return secondToLastLetter + lastLetter

    #hello
    #01234
    #len(hello) -> 5

def endsWithLY(word):
    #should return True if the word ends with ly
    #False if it doesn't

    #beautifully -> True
    #Beautiful -> False

    lastTwoLetters = lastTwo(word)
    if lastTwoLetters == "ly":
        return True
    else:
        return False

def firstAlastB(a, b):
    #a -> hello
    #b -> goodbye
    #firstAlastB(a, b) -> "he"

    first = a[0]
    last = b[len(b) - 1]
    return first + last


def middleTwo(string):
    middle = len(string) /2

    start = middle - 1
    stop = middle + 1
    return string[start : stop]

print ("billy", "yellow")

def fancyconcat(str1, str2):
    last = str1[len(str1) - 1]
    first = str2[0]
    if last == first:
        firstBit = str1[0:len(str1) - 1]
        lastBit = str2[1 : len(str2)]
        return firstBit + lastBit
    else:
        return str1 + str2


def swap(word):
    #hello
    #swap(hello) -> oellh
    firstLetter = word[0]
    lastLetter = word[len(word) - 1]
    middle = word[1:len(word) -1]
    return lastLetter+middle+firstLetter

def switch(word):
    endWord = word[0:len(word) - 2]
    firstTwo = word[0:2]
    return endWord+firstTwo

def swapLastTwo(string):
    #swapLastTwo("hello") -> helol
    first = string[0:len(string) - 2]
    middle = string[len(string)- 2]
    last = string[len(string) - 1]
    return first+last+middle


print (endsWithLY("beautifully"))
print (endsWithLY("beautiful"))
print (firstAlastB("hello","goodbye"))
print (fancyconcat("billy", "yellow"))
print (fancyconcat("billy" , "blue"))
print(swap("hello"))
print (switch("yellow"))
print (swapLastTwo("hello"))
