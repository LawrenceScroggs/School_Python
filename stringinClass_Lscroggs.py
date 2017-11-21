# stringsinClass_Lscroggs
# Allowing user to input alpha and numeric characters
# user then select from menu to change the strings outputs
# 11/17/17
# Python 3.6.2
import math
print("Strings in Class")
print("This program will show you 14 different string functions.")
      
def main():
    
    user_input = input("Please enter a string you would like to use.  ")
    menu(user_input)
    user_output(user_input)
    again()
def menu(user_input):
    print("Here is a list of the possible string functions and what they do.")
    print("1. Make everything uppercase.\n"
        "2. Make the first letter uppercase.\n"
        "3. Make everything lowercase.\n"
        "4. Test to see if string is all alphabetic.\n"
        "5. Test to see if string is all numeric.\n"
        "6. Test to see if sting is all uppercase.\n"
        "7. Test to see if string is all lowercase.\n"
        "8. Returns true if string is all whitespace."
        "9. Replaces 'a' with 'X'.\n"
        "10. Counts how many 'a' are in string.\n"
        "11. Will take the letter 'o' out of string."
        "12. Returns true if all digits.\n"
        "13. Returns true if all decimal.\n"
        "14. Swaps uppercase and lowercase letters.\n")
def user_output(user_input):
    user_string = int(input("Please select from 1 - 14 to change your string.   "))
    
    while user_string < 0 or user_string > 14:
        print("Invalid Input")
        return user_output
    
    #cannot figure out how to stop user from inputing string or float
    #will keep testing

    if user_string == 1:
        print("",user_input.upper(),"")
        return again()
    elif user_string == 2:
        print("",user_input.title(),"")
        return again()
    elif user_string == 3:
        print("",user_input.lower(),"")
        return again()
    elif user_string == 4:
        print("",user_input.isalpha(),"")
        return again()
    elif user_string == 5:
        print("",user_input.isnumeric(),"")
        return again()
    elif user_string == 6:
        print("",user_input.isupper(),"")
        return again()
    elif user_string == 7:
        print("",user_input.islower(),"")
        return again()
    elif user_string == 8:
        print("",user_input.isspace(),"")
        return again()
    elif user_string == 9:
        print("",user_input.replace("a","X"))
        return again()
    elif user_string == 10:
        print("",user_input.count("a"),"")
        return again()
    elif user_string == 11:
        print("",user_input.strip("o"),"")
        return again()
    elif user_string == 12:
        print("",user_input.isdigit(),"")
        return again()
    elif user_string == 13:
        print("",user_input.isdecimal(),"")
        return again()
    elif user_string == 14:
        print("",user_input.swapcase(),"")
        return again()
    else:
        print("Invalid Input")
        return again()
def again():
    repeat = input("Would you like to run the program again? Yes or No?    ")
    while repeat.lower() == 'yes':
        return main()
    if repeat.lower() == 'no':
            exit()
    else:
        print("Invalid Input")
        return again()       


main()
