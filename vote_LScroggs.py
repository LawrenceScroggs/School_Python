#File:vote_LScroggs.py
#Description: Checking 3 criteria for legal voting
#Author: Lawrence Scroggs
#Date: 10/16/17
#Compiler: Python 3.6.2
#Could not get it to run sucessfully
#wont differentiate between lowercase and uppercase
#forgot to put () after variable.lower
print("Are you old enough to vote?\n\n")
print("Let's see if you meet the 3 critera required.\n\n")
str_age = input("What is your age? (Please use whole numbers.)  ")
if str_age.isdigit():
    age = int(str_age)
else:
    print("Invalid input.")
    exit()

if age >= 18 and age < 120:
    print('')
else:
    print("Sorry you do not meet the requirements")
    exit()
us_citizen = input("Are you a U.S. citizen?  ")
us_citizen = us_citizen.lower()
if us_citizen == "yes":
    print('')
elif us_citizen == "no":
    print("Sorry you do not meet the requirements")
    exit()
else:
    print("Sorry you do not meet the requirments")
    exit()
vote = input("Are you registered to vote?  ")
vote = vote.lower()
if vote == "yes":
    print("You meet all three requirements.  Go out and VOTE!!:)")
elif vote == "no":
    print("Sorry you do not meet the requirements")
    exit()
else:
    print("Sorry you do not meet the requirements")
    exit()
