def initials(firstName, middleName, lastName):
    firstInitial = firstName[0:1]
    middleInitial = middleName[0]
    lastInitial = lastName[0]
    return firstInitial + middleInitial + lastInitial

print (initials("Ryan", "Samuel", "Reiss"))

def fancyInitials(fromTheEnd, first, middle, last):
    if fromTheEnd == False:
        answer = initials(first, middle, last)
        return answer
    else:
        lastFirstInitial = first[len(first) - 1]
        lastMiddleInitial = middle[len(middle) - 1]
        lastLastInitial = last[len(last) - 1]
        return lastFirstInitial + lastMiddleInitial + lastLastInitial

print (fancyInitials(True, "Ryan", "Samuel", "Reiss"))
