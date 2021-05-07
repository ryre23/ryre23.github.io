def printString(word):
    basket = ""
    for index in range(len(word)):
        basket = basket + word[index] + "\n"
    return basket

print(printString("hello"))


def printEveryOther(word):
    basket = ""
    for index in range(0, len(word), 2):
        basket = basket + word[index] + "\n"
    return basket

print(printEveryOther("hello"))


def printBackwards(word):
    basket = ""
    for index in range(len(word) -1 , -1 , -1):
        basket = basket + word[index] + "\n"
    return basket

print(printBackwards("hello"))

def printDoubled(word):
    basket = ""
    for index in range(0, len(word)):
        #print(word[index])
        #print(word[index])
        basket = basket + word[index] + "\n" + word[index] + "\n"
    return basket

print(printDoubled("hello"))


def containsA(word):
    basket = False
    for index in range(len(word)):
        if word[index] == "a":
            basket = True
    return basket

print(containsA("grape"))
print(containsA("kiwi"))

def containsVowel(word):
    basket = False
    for index in range(len(word)):
        if word[index] == "a" or word[index] == "e" or word[index] == "i" or word[index] == "o" or word[index] == "u":
            basket = True
    return basket

print(containsVowel("grape"))
print(containsVowel("jklmn"))


def countVowel(word):
    basket = 0
    for index in range(len(word)):
        vowel = word[index] == "a" or word[index] == "e" or word[index] == "i" or word[index] == "o" or word[index] == "u"
        if vowel == True:
            basket = basket + 1
    return basket

print(countVowel("grape"))

def containsKiwi(word):
    basket = False
    for index in range(0, len(word) - 1):
        window = word[index: index+4]
        if window == "kiwi":
            basket = True
    return basket

print(containsKiwi("ilovekiwi"))


def countKiwi(word):
    basket = 0
    for index in range(0, len(word) - 1):
        window = word[index: index+4]
        if window == "kiwi":
            basket = basket + 1
    return basket

print(countKiwi("kiwikiwikiwi"))


def countTarget(word, target):
    basket = 0
    for index in range (0, len(word) - 1):
        stoppingPoint = len(target) + index
        window = word[index : stoppingPoint]
        if window == target:
            basket = basket + 1
    return basket

print(countTarget("hellohello" , "ll"))


def containsAdjPair(word):
    basket = False
    for index in range(0, len(word) - 1):
        stoppingPoint = index + 2
        window = word[index : stoppingPoint]
        if window[0]== window[1]:
            basket = True
    return basket

print(containsAdjPair("hello"))
print(containsAdjPair("grape"))

