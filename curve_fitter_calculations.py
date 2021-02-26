# Curve Fitter Table Calculator
# Written By Dhrumil Mistry

############### Importing Modules  ###############
from statistics import mean

############### FUNCTION DEFINITIONS ###############

# returns data in form of list, n: total number of data
def get_data_list(n):
    data_list = list()
    for i in range(n):
        data_temp = float(input())
        data_list.append(data_temp)

    return data_list


# returns power powered list
def get_powered(data_list, power):
    powered_list = list()
    for data in data_list:
        powered_list.append(data**power)

    return powered_list

# returns mulitplied list
def get_list_mult(list1, list2):
    return [a * b for a, b in zip(list1, list2)]


############### DRIVER CODE ###############

# Total Number
n = int(input('[+] Enter total data number : '))

# taking data
print("[+] Enter DATA for X: ")
x = get_data_list(n)

print("[+] Enter DATA for Y: ")
y = get_data_list(n)

# Printing X, Y list
print('X : ', x)
print('Y : ', y)


# calulating required

    # for X^2, X^3, X^4
x_square = get_powered(x, 2)
x_cube = get_powered(x, 3)
x_quad = get_powered(x, 4)

    # for XY, X^2*Y
xy = list(get_list_mult(x,y))
x_square_y = list(get_list_mult(x_square, y))

    # mean X, Y
x_bar = mean(x)
y_bar = mean(y)


# printing data
print('DATA -> Total')
print('X^2 : ',x_square,' ->\t ', sum(x_square))
print('X^3 : ', x_cube,' ->\t ', sum(x_cube))
print('X^4 : ', x_quad,' ->\t ', sum(x_quad))
print('X.Y : ', xy,' ->\t ', sum(xy))
print('X^2.Y : ', x_square_y,' ->\t ', sum(x_square_y))

print('X bar = ', x_bar)
print('Y bar = ', y_bar)
