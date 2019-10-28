from random import *

def S_Sort(listin):
    while not S_InOrder(listin):
        S_Shuffle(listin)
    return listin

def S_InOrder(listin):
    for i in range(len(listin) - 1):
        if listin[i] > listin[i + 1]:
            return False
    return True

def S_Search(listin, target):
    found = False
    while not found:
        val = randint(0, len(listin)-1)
        if listin[val] == target:
            return val

def S_RanInt(lower, upper):
    return randint(lower, upper)

def S_Shuffle(listin):
    return shuffle(listin)