import math
def findarea(input):
    pass
def findcirumfrence(inputvar):
    findinginputdef = True
    while findinginputdef == True:
        inputdef = input("Diameter/Circumfrence/Raduis/Area(D/C/R/A): ").strip().lower()
        if inputdef == "D" or inputdef == "C" or inputdef=="R":
            findinginputdef = False
            break
    if inputdef == "c":
        return "You Already have the Circumfrence Silly"
    if input == "r":
        val = 2 * math.pi * inputvar
        return val,round(val), round(val,2)
    if input == "d":
        r = inputvar/2
        val = 2 * math.pi*r
        return val,round(val), round(val,2)
    if input == "A"



