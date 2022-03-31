#   Write a program that uses input to prompt a user for their name and welcomes them
#   Write a program to prompt the user for hours and rate per hour to computer gross pay (round to tenths)

name = input ('Hello, and welcome to Aquisitions Incorporated, please enter your name: ')   #Takes string input from user, in this case their name

hours = input ('How many hours did you work at your last job?: ')                               # Takes two more inputs, hours worked and money obtained
money = input ('How much were you paid in total?: ')

gross = (float(money) / float(hours))                                                               # Takes the input values for hours worked and money obtained, converts into integers and divides
pay = round(gross, 2)                                                                               # Rounds the gross value to the hundredth digit (0.00)

welcome = 'Welcome, {}, to our wonderful corporation!'.format(name)                              # .Format(variable) Is used to insert variables into strings!!!
promise = "We'll make sure to pay you well! more than ${} an hour at least!".format(pay)            # Using .Format again because of pay values


print(welcome)                                                          # Prints the message with the name variable in it!
print(promise)

input("-Press enter to end initiaion-")