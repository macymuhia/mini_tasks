# a program that asks the user for a number
# and then prints out a list of all the divisors of that number


number = input('Please input a number: ')

x = number / 2

div_list = []

for y in range(1, x+1):
    if number % y == 0:
        div_list.append(y)
print (div_list)