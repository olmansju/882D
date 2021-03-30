import operator
import random
import math

def difficultyFinder(firstNum, secondNum, operate):
    if (firstNum + secondNum) < 11:
        dval = 10
    elif ((len(str(firstNum)) + len(str(secondNum))) // 2) == 1:
        dval = 11
    elif ((len(str(firstNum)) + len(str(secondNum))) // 2) == 2:
        dval = 20
        if (int(str(firstNum)[-1]) + int(str(secondNum)[-1])) > 9:
            dval = dval + 1
        if (int(str(firstNum)[-2]) + int(str(secondNum)[-2])) > 9:
            dval = dval + 1
    elif ((len(str(firstNum)) + len(str(secondNum))) // 2) == 3:
        dval = 30
        if (int(str(firstNum)[-1]) + int(str(secondNum)[-1])) > 9:
            dval = dval + 1
        if (int(str(firstNum)[-2]) + int(str(secondNum)[-2])) > 9:
            dval = dval + 1
        if (int(str(firstNum)[-3]) + int(str(secondNum)[-3])) > 9:
            dval = dval + 1
    elif ((len(str(firstNum)) + len(str(secondNum))) // 2) == 4:
            dval = 40
            if (int(str(firstNum)[-1]) + int(str(secondNum)[-1])) > 9:
                dval = dval + 1
            if (int(str(firstNum)[-2]) + int(str(secondNum)[-2])) > 9:
                dval = dval + 1
            if (int(str(firstNum)[-3]) + int(str(secondNum)[-3])) > 9:
                dval = dval + 1
            if (int(str(firstNum)[-4]) + int(str(secondNum)[-4])) > 9:
                dval = dval + 1
    else:
        dval = 50
    return dval

def roundup(x, y):
    return int(math.ceil(x / float(y))) * y

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, "/": operator.floordiv}

def d1AddDistractor(firstNum, secondNum):
    if (int(str(firstNum)[-1]) + int(str(secondNum)[-1])) > 9:
        # this is the distractor for when the student forgets to carry the 1 to the 10s column addition
        d1AD = (firstNum + secondNum) - 10
    elif (firstNum > 9) and (secondNum > 9):
        if (int(str(firstNum)[-2]) + int(str(secondNum)[-2])) > 9:
            # same as above but forgetting to carry the 1 in the 100s column addition
            d1AD = (firstNum + secondNum) - 100
        else:
            d1AD = (firstNum + secondNum) + random.randrange(-5, 5, 3)
    else:
        d1AD = (firstNum + secondNum) + random.randrange(-5, 5, 3)
    return d1AD

def d2AddDistractor(firstNum, secondNum):
    if (int(str(firstNum)[-1]) + int(str(secondNum)[-1])) > 9:
        # this is the distractor for when the student forgets to finish partial sums addition
        d2AD = int(str(firstNum + secondNum)[:-1] + str(int(str(firstNum)[-1]) + int(str(secondNum)[-1])))
    elif (9 < firstNum) and (9 < secondNum):
        if (int(str(firstNum)[-2]) + int(str(secondNum)[-2])) > 9:
            # this adds the second column with the first column in a buggy way via partial sums addition
            d2AD = int(str(firstNum + secondNum)[:-2] + str((int(str(firstNum)[-2]) + int(str(secondNum)[-2])) + (int(str(firstNum)[-1]) + int(str(secondNum)[-1]))))
        else:
            places = (len(str(firstNum)) + len(str(secondNum))) // 2
            i = 0
            d2AD = 0
            while i < places:
                d2AD = d2AD + int(str(firstNum)[i]) + int(str(firstNum)[i])
                i = i + 1
    else:
        places = (len(str(firstNum)) + len(str(secondNum))) // 2
        i = 0
        d2AD = 0
        while i < places:
            d2AD = d2AD + int(str(firstNum)[i]) + int(str(firstNum)[i])
            i = i + 1
    return d2AD

def d3AddDistractor(firstNum, secondNum):
    if ((len(str(firstNum)) + len(str(secondNum))) // 2) == 2:
        # this is the distractor for when the student uses estimation
        d3AD = roundup(firstNum + secondNum, 10)
    elif ((len(str(firstNum)) + len(str(secondNum))) // 2) == 1:
        # this is the distractor for when the student uses estimation
        if (firstNum + secondNum) != 10:
            d3AD = 10
        else:
            d3AD = 9
    elif ((len(str(firstNum)) + len(str(secondNum))) // 2) == 3:
        # this is the distractor for when the student uses estimation
        d3AD = roundup(firstNum + secondNum, 100)
    elif ((len(str(firstNum)) + len(str(secondNum))) // 2) == 4:
        # this is the distractor for when the student uses estimation
        d3AD = roundup(firstNum + secondNum, 1000)
    else:
        d3AD = roundup(firstNum + secondNum, 10000)
    return d3AD

def distractorlist(firstNum, secondNum, operate):
    if operate == '+':
        d1 = d1AddDistractor(firstNum, secondNum)
        d2 = d2AddDistractor(firstNum, secondNum)
        d3 = d3AddDistractor(firstNum, secondNum)
        return [d1, d2, d3]
    elif operate == '-':
        # for later
        e = 1
    elif operate == '*':
        # for later
        e = 1
    elif operate == '/':
        # for later
        e = 1
    else:
        return []

def generate_item_bank(itemtotal, operate):
    #make an item bank
    bankdict = {
        "firstNum" : 0,
        "secondNum" : 0,
        "operator" : operate,
        "answer" : 0,
        "distractor1": 1,
        "distractor2": 2,
        "distractor3": 3,
        "difficulty" : 0
    }
    banklist = [bankdict]
    astart = 5
    astep = 3
    a = range(astart, (itemtotal + astart) * (astep), astep)
    print(len(a))
    bstart = 1
    bstep = 2
    b = range(bstart, (itemtotal + bstart) * (bstep), bstep)
    print(len(b))

    i = 0
    while i < (itemtotal -1):
        bankdict = {}
        print(i)
        dL = distractorlist(a[i], b[i], operate)
        difLevel = difficultyFinder(a[i], b[i], operate)
        bankdict = {
            "firstNum": a[i],
            "secondNum": b[i],
            "operator": operate,
            "answer": ops[operate](a[i], b[i]),
            "distractor1": dL[0],
            "distractor2": dL[1],
            "distractor3": dL[2],
            "difficulty": difLevel
        }
        i = i + 1
        banklist.append(bankdict)
    return banklist

rr = generate_item_bank(39, '+')

print(rr)
