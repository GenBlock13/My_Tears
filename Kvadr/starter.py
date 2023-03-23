from math import sqrt
from cmath import sqrt


# class BugStatus(enum.Enum):
#     INCORRECT_INPUT = "Incorrect input"
#     INCORRECT_DATA = "Incorrect Data"
#     INCORRECT_OUTPUT_TYPE = "Unknown output type"
#     INCORRECT_OUTPUT_DATA = "No output data"
#
# def ErrorOutput(reason:str):
#     raise Exception(reason)
'''
Burned lives
1. -0 1 2 1
2. -1 1 1 1
3. -1 0 0 0 множество корней
4.-1 a b c
5.


'''

def input_data():
    s = input('$: \n')
    numb = s.split(' ')
    global a,b,c
    a=float(numb[0])
    b=float(numb[1])
    c=float(numb[2])

    return a, b, c

def solve_linear(b,c):
    global x
    if b == 0 and c == 0:
        x = "Many real roots"
        return x
    if b == 0:
        x = "Can't be solved"
        return x
    else:
        x = (-c/b)
    return x

def solve_discrim(a, b, c):
    dscrm = b*b - 4*a*c
    x1 = 0
    x2 = 0
    if dscrm < 0:
        x1 = (-b - sqrt(dscrm)) / (2 * a)
        x2 = (-b + sqrt(dscrm)) / (2 * a)
        x1 = str(x1)
        x2 = str(x2)
        x1 = x1.replace('j', 'i')
        x2 = x2.replace('j', 'i')
        return x1, x2
    elif dscrm == 0:
        x1 = (-b) / (2 * a)
        x2 = (-b) / (2 * a)
        return x1, x2
    else:
        x1 = ((-b) - dscrm ** 0.5) / (2 * a)
        x2 = ((-b) + dscrm ** 0.5) / (2 * a)
        return x1, x2


def solve_equation(a, b, c):
    if a == 0:
        solve_linear(b,c)
        return x
    else:
        solve_discrim(a,b,c)
        return x1, x2


input_data()
solve_equation(a, b, c)

if a == 0:
    print(x)
else:
    print(x1, x2)