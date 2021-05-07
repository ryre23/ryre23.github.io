def testForTarget(str, target):
    basket=[]
    for index in range(0, len(str)):
        stoppingPoint = index +len(target)
        window = str[index:stoppingPoint]
        if window == target:
            return True
    else:
        return False

print(testForTarget("Giraffe", "raf"))



def countAdjDuplicates(str):
    basket = 0
    for index in range(0, len(str)-1):
        window = index + 1
        if str[index] == str[window]:
            basket = basket + 1
    return basket

print(countAdjDuplicates("Good Guy Gregg"))


def ABCTester(str):
    basketA = 0
    basketB = 0
    basketC = 0
    for index in range(0, len(str)):
        if str[index] == "A":
            basketA = basketA+1
        if str[index] == "B":
            basketB = basketB+1
        if str[index] == "C":
            basketC = basketC+1

    if basketA > basketB and basketC:
        return "A"
    if basketB> basketA and basketC:
        return "B"
    if basketC > basketA and basketB:
        return "C"

print(ABCTester("AAABBBBCCC"))
