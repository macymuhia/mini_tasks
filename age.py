# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.


name = input('Please enter your name: ')

age = int(input('Please enter your age: '))

new_age = (100 - age) + 2019

print ('Hi %s, you will turn 100 years old in the year %d' % (name, new_age))
