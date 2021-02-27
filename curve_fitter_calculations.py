# Curve Fitter Table Calculator
# Written By Dhrumil Mistry


############### Importing Modules  ###############
from statistics import mean
from prettytable import PrettyTable

############### FUNCTION DEFINITIONS ###############


# returns data in form of list, n: total number of data
def get_data_list(n):
    data_list = list()
    for i in range(n):
        data_temp = input()
        data_list.append(float(data_temp))

    return data_list


# returns power powered list
def get_powered(data_list, power):
    powered_list = list()
    for data in data_list:
        powered_list.append(round(data**power,2))

    return powered_list


# returns mulitplied list
def get_list_mult(list1, list2, n):
    mult = []
    for i in range(n):
        mult.append(round(list1[i]*list2[i],2))

    return mult


# returns a new list with elements list1 - list2
def sub_num(list1, num):
    return [ele - num for ele in list1]

# returns list with numbers upto 2 decimal digits
def get_two_digit_list(my_list):
    return [ '%.2f' % elem for elem in my_list ]

# prints formatted table
def print_table(x,y,x_square,x_cube,x_quad,xy,x_square_y,varX,varY):
    table = PrettyTable()
    table.field_name = [varX, varY, varX+"^2", varX+"^3", varX+"^4", varX+"."+varY, varX+"^2."+varY]
    table.add_column(varX,x)
    table.add_column(varY,y)
    table.add_column(varX+"^2",x_square)
    table.add_column(varX+"^3",x_cube)
    table.add_column(varX+"^4",x_quad)
    table.add_column(varX+"."+varY,xy)
    table.add_column(varX+"^2."+varY,x_square_y)

    total_table = PrettyTable()
    total_table.field_names = [varX, varY, varX+"^2", varX+"^3", varX+"^4", varX+"."+varY, varX+"^2."+varY]

    total_list = [sum(x),sum(y),sum(x_square),sum(x_cube),sum(x_quad),sum(xy),sum(x_square_y)]
    total_table.add_row( [round(ele,2) for ele in total_list] )

    print("Table:")
    print(table)
    print("Total")
    print(total_table)


############### DRIVER CODE ###############
print('<----- Curve Fitter Calculator ----->')

# Total Number
n = int(input('[+] Enter total data number : '))

# taking data
print("[+] Enter DATA for X: ")
x = get_data_list(n)

print("[+] Enter DATA for Y: ")
y = get_data_list(n)

# calulating required terms

    # for X^2, X^3, X^4
x_square = get_powered(x, 2)
x_cube = get_powered(x, 3)
x_quad = get_powered(x, 4)

    # for XY, X^2*Y
xy = get_list_mult(x, y, n)
x_square_y = get_list_mult(x_square, y, n)

    # mean X, Y
x_bar = mean(x)
y_bar = mean(y)

    # u = x - xbar
    # v = v - ybar
u = sub_num(x, x_bar)
v = sub_num(y, y_bar)

    # 2, 3, 4 powers of u
u_square = get_powered(u, 2)
u_cube = get_powered(u, 3)
u_quad = get_powered(u, 4)

    # for UV, U^2*V
uv = list(get_list_mult(u, v, n))
u_square_v = list(get_list_mult(u_square, v, n))


# Printing Table
print_table(x,y,x_square,x_cube,x_quad,xy,x_square_y,'X','Y')
    # printing mean x and y

print()
print('X bar = ' + str(x_bar))
print('Y bar = ' + str(y_bar))
print()

print_table(u,v,u_square,u_cube,u_quad,uv,u_square_v,'U','V')
