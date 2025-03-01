import math
def findarea(input):
    pass
def findcirumfrence(inputvar):
    findinginputdef = True
    while findinginputdef == True:
        inputdef = input("Diameter/Circumfrence/Raduis/Area(D/C/R/A): ").strip().lower()
        if inputdef == "d" or inputdef == "c" or inputdef=="r" or inputdef == "a":
            findinginputdef = False
            break
    if inputdef == "c":
        return "You Already have the Circumfrence Silly"
    if inputdef == "r":
        val = 2 * math.pi * inputvar
        return val,round(val), round(val,2)
    if inputdef == "d":
        r = inputvar/2
        val = 2 * math.pi*r
        return val,round(val), round(val,2)
    if inputdef == "a":
        r = math.sqrt(inputvar/math.pi)
        val = 2*math.pi*inputvar
        return val,round(val), round(val,2)
def findraduis(inputvar):
    findinginputdef = True
    while findinginputdef == True:
        inputdef = input("Diameter/Circumfrence/Raduis/Area(D/C/R/A): ").strip().lower()
        if inputdef == "d" or inputdef == "c" or inputdef=="r" or inputdef == "a":
            findinginputdef = False
            break
        if inputdef == "r":
            return "You already Have the raduis"
        if inputdef == "d":
            return inputvar/2, math.round(inputvar/2,2)
        if inputdef == "a":
            r = math.sqrt(inputvar/math.pi)
            return r, round(r,2)
        




