# Jwaun Huntley
# 3/7/19

# Takes a list and checks for a value

def listCheck(n):
    for x in n:
        if x == 5:
            return True

numberList = [1, 5, 3, 4, 3]

print (listCheck(numberList))
