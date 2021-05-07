def containsTarget(str, target):
    for index in range(0, len(str)):
        stoppingPoint = index + len(target)
        window = str[index:stoppingPoint]
        if window == target:
            return True
    else:
        return False


print (containsTarget("ethan","than"))


def countXY(str):
    basketx = 0
    baskety = 0
    for index in range(0, len(str)):
        if str[index] == "x":
            basketx = basketx + 1
        if str[index] == "y":
            baskety = baskety+1
    if basketx == baskety:
        return True
    else:
        return False

print(countXY("xxxyyyxxxyyy"))
