favoriteFood = input("What is your favorite food? ")

#concatenate

sentence = "My favorite food is: " + favoriteFood

#indexing
#index -> a spot for a specific letter in a string
#valid index range -> 0, 

firstLetter = favoriteFood[0]

print (firstLetter)

lastIndex = len(favoriteFood) - 1
lastLetter = favoriteFood[lastIndex]

print (lastLetter)

numLetters = len(favoriteFood)

print (numLetters)

firstThree = favoriteFood[0:3]

print(firstThree)

lastThree = favoriteFood[numLetters - 3:numLetters]

print(lastThree)

firstHalf = favoriteFood[0:numLetters//2]

print(firstHalf)

secondHalf = favoriteFood[numLetters // 2 : numLetters]
print(secondHalf)

test = favoriteFood * 5
print(test)
