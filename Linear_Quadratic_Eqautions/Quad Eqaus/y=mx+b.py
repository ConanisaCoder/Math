from fractions import Fraction
from math import *
def find_intercept_Origin(x,y):
    match x,y:
        case 0,0:
            return "Origin"
        case 0,y:
            return "Y-Intercept"
        case x,0:
            return "X-Intercept"
        case _:
            return "Regualar"
def find_slope(x,y,x_2,y_2): #bugged returns frac_slope as slope
    '''Function to Find Slope'''
    slope = ((y_2 - y)/(x_2 - x))
    '''If slope is a decimal convert to fraction and retrun vaule'''
    if slope == float:
        frac_slope = str(Fraction(slope))
        return frac_slope
    else:
        return slope
def find_x_y_intercept(x_coefficient,y_coefficient,vaule):
    while True:
        try:
            find_x_y = int(input("What do want to find(x (1) /y (2))?: "))
            break
        except ValueError:
            print("Enter Int")
    if find_x_y < 1:
        find_x_y = 1
        print("Input less than one input is now One (Finding X).")
    elif find_x_y > 2:
        print("Input greated than two input is now One (Finding Y).")
    match find_x_y:
        case 1:
            x_intercept = vaule / x_coefficient
            if abs(x_intercept) < 1 or x_intercept == float:
                return str(Fraction(x_intercept))
            else:
                return x_intercept
        case 2:
            y_intercept = vaule / y_coefficient
            if abs(y_intercept) < 1 or y_intercept ==  float:
                return str(Fraction(y_intercept))
            else:
                return y_intercept
def solve_sys_eqau_simple(b_val,m_val,m_val2,b_val2):
    print(f"y = {m_val}x + {b_val}")
    print(f"y = {m_val2}x +{b_val2}")
    m_total = (m_val) - (m_val2)
    b_total = (b_val2) - (b_val)
    x = b_total / m_total
    print(x)
    y = m_val * x + b_val
    print(y)
    if y == float:
        y = Fraction(y)
    if x == float:
        x = Fraction(x)
    return f"({x},{y})"
def Forms_of_Linear_Eqau(y_1,y_2,x_1,x_2):
    print("Options\n(1) Point-Slope Form\n(2) Slope-Intercept Form\n(3) Standard Form\n(4) All Three")
    while True:
        try: 
            option = int(input("Enter option: "))
            break
        except ValueError:
            print("Enter Int")
    if option == 1:
        slope = (y_2 - y_1) / (x_2 - x_1)
        return f" (y  - {y_1}) = {slope}(x - {x_1}) "
    if option == 2: 
        slope = (y_2 - y_1) / (x_2 - x_1)
        b = (slope *x_1) -y_1 
        return f"y = {slope}x + {b}"
    if option == 3:
        slope = (y_2 - y_1) / (x_2 - x_1)
        slope *= -1
        b = (slope *x_1) -y_1 
        return f"y + {slope}x = {b}"
    if option == 4:
        list_ret = []
        slope = (y_2 - y_1) / (x_2 - x_1)
        list_ret.append(f" (y  - {y_1}) = {slope}(x - {x_1}) ")
        slope = (y_2 - y_1) / (x_2 - x_1)
        b = (slope *x_1) -y_1 
        list_ret.append(f"y = {slope}x + {b}")
        slope = (y_2 - y_1) / (x_2 - x_1)
        slope *= -1
        b = (slope *x_1) -y_1 
        list.ret.append(f"y + {slope}x = {b}")
        return "\n".join(list_ret)

def find_lin_eqau_val(y_1,y_2,x_1,x_2):
    pass
'''
    list_value = []
    slope = (y_2 - y_1) / (x_2 - x_1)
    y-intercept = (slope *x_1) -y_1 
    retrun slope, list_value
'''
    

