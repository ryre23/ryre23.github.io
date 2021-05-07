#str -> string -> text
name = input("What is your name?")

print ("hello " + name)

brothers = input("How many brothers do you have?")

print ("You have " + brothers + "brothers")

sisters = input("How many sisters do you have")

print ("You have " + sisters + "sisters")

numBrothers = int(brothers)
numSisters = int(sisters)
numSiblings = numBrothers + numSisters

siblings = str(numSiblings)

print ("You have " + siblings + "siblings")

#Rule: + -> str + str = concatenation (gluing)
# + -> int + int = addition
# + -> int + str = ERROR!

dogs = input("How many dogs do you have?")

print ("You have " + dogs + "dogs")

cats = input("How many cats do you have")

print ("You have " + cats + "cats")

fish = input("How many fish do you have?")

print ("You have " + fish + "fish")

numDogs = int(dogs)
numCats = int(cats)
numFish = int(fish)

numPets = numDogs + numCats + numFish

pets = str(numPets)

print ("You have " + pets + "pets")


year = input("What year were you born?")
yearNum = int(year)
myAgeThisYear = 2021 - yearNum
print ("I turn " + str(myAgeThisYear) + " this year")

#Rule (required)
#1. NO SPACES
#2. Must start with a letter (4chan) is not a valid name)
#3. Alphanumeric (Alpha = letters) (numeric = numbers)(also underscores "_")

#Convention (suggestions)
#1. descriptive
#2. camelCase -> capitalizing the first letter of each word (except the first)
#2b. underscores as spaces -> my_age_this_year
#3. typically, start with a lowercase letter



