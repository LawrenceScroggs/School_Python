#File:larger_lscroggs.py
#Description: Checking the values of two digits to determine which
#is larger
#Author:Lawrence Scroggs
#Date: 10/16/17
#Compiler: Python 3.6.2
#Couldnt figure out how to add float input
#got float to work couldnt block string
#tried isdecimal and isfloat instead of isdigit.  Did not work.
#isntructed user to enter whole numbers
print("Find out which number is great""\n\n")
number_one = input("Please enter your first whole number  ")
print('')
number_two = input("Please enter your second whole number   ")
print('')
if number_one.isdigit():
    one = int(number_one)
else:
    print("Invalid Input")
    exit()
if number_two.isdigit():
    two = int(number_two)
else:
    print("Invalid Input")
    exit()
if one > two:
    print('',one,"is greater than",two,'')
elif one < two:
    print('',two,"is greater than",one,'')
elif one == two:
    print("The numbers are equal")
else:
    print("Invalid Input")
    exit()
