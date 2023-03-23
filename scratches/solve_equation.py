'''
Burned lives
1. -0 1 2 1
2. -1 1 1 1
3. -1 0 0 0 множество корней
4.-1 a b c
5.


'''

from math import sqrt
from cmath import sqrt


def solve_linear(b,c):
    if b == 0 and c == 0:
        linear_root = "Many roots"
        return linear_root
    if b == 0:
        linear_root = "Can't be solved"
        return linear_root
    else:
        linear_root = (-c/b)
    return linear_root


def solve_discrim(a, b, c):
    dscrm = b*b - 4*a*c
    x1 = 0
    x2 = 0
    if dscrm < 0:
        x1 = str((-b - sqrt(dscrm)) / (2 * a))
        x2 = str((-b + sqrt(dscrm)) / (2 * a))
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
        return solve_linear(b,c)
    else:
        return solve_discrim(a,b,c)

    
def input_data():
    my_input = input().split(' ')
    if len(my_input) == 3:
        return my_input     
    else:
        print('Use 3 arguments')
        return


def make_data(my_input):
    valid_symbols = {'inf', '-inf', '+inf', 'nan', 'NAN', 'nAn','NaN', 'Nan', '-', '+'}
    my_data = (''.join(my_input)).replace('-', '').replace('e','').replace('.','').replace('inf', '')
    my_set = set(my_input)
    if  my_data.isnumeric or not my_set.difference(valid_symbols):
        a=float(my_input[0])
        b=float(my_input[1])
        c=float(my_input[2])
        return a, b, c
    else:
        print('Invalid input')
        return 


my_numbers = input_data()
if my_numbers:
    if make_data(my_numbers):
        a, b, c = make_data(my_numbers)
        print(solve_equation(a, b, c))

