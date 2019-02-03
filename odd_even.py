# Ask the user for a number.
# Depending on whether the number is even or odd,
# print out an appropriate message to the user telling them whether the number is even or odd.


y = int(input('Please enter a number: '))

def res(x):
    if (x % 2) == 0:
        return ('%d is an even number' % x)
    else:
        return ('%d is an odd number' % x)

if isinstance(y, int):
    print(res(y))

else:
    print ('That is not a number')
