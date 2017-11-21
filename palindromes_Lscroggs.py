#palindromes_Lscroggs
#program to check if user input is a palindrome
#11/18/17
#Python3.6.2
print("Welcome to the Palindrome Program.\n")
print("pal·in·drome")
print("ˈpalənˌdrōm/")
print("noun")
print("noun: palindrome; plural noun: palindromes")
print("a word, phrase, or sequence that reads the same backward\n"
      "as forward, e.g., madam or nurses run.\n\n")
def main():
    user_input = 'yes'
    while user_input == 'yes':
        run_ptest()
        user_input = again()
    exit

def run_ptest():
    pal_1 = input("Please enter your possible Palindrome\n"
                  "(no numbers or punctuation)  ")
    pal_1 = pal_1.strip(' ')
    pal_2 = pal_1[-1::-1]
    pal_2 = pal_2.strip(' ')
    if pal_1.strip(" ") == pal_2.strip(" "):
        print("This is a Palindrome :) ")
    else:
        print("This is not a Palindrome")
    print("Forwards:",pal_1.strip(' '),"")
    print("Backwards:",pal_2.strip(' '),"")
def again():
    user_input2 = input("Would you like to run the program again?   ")
    if user_input2 == 'yes' or user_input2 == 'no':
        return user_input2
    else:
        print("Invalid Input")
        return again()
main()
