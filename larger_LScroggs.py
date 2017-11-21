#File:vote_LScroggs.py
#Description: Checking 3 criteria for legal voting
#Author: Lawrence Scroggs
#Date: 10/16/17
#Compiler: Python 3.6.2
#could not figure how to add float input to be compared
# got the float in there cannot figure how to block strings
#tried isdecimal and isfloat instead of is digit. did not solve issue.
#instructed user to enter whole numbers
print("Find out which number is greater""\n\n")
number_one = input("Please enter your first whole number   ")
print('')
number_two = input("Please enter your second whole number  ")
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
    exit ()
