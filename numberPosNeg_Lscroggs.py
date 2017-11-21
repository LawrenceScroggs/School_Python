#numberPosNeg_Lscroggs.py
#Creating a loop until user inputs 0
#keeps track of amount of negative and positive integers
#Lawrence Scroggs
#Python 3.6.2
import math
print("Entering positive of negative numbers.\n\n")

def main():
    pos_num = 0
    neg_num = 0
    input_num = 1
    while input_num != 0:
        input_num = int(input("Enter a positive or negative whole number, type 0 to quit.    "))
        if input_num > 0:
            pos_num += 1
        elif input_num < 0:
            neg_num += 1

    print("There are",pos_num," positive numbers.")
    print("There are ",neg_num," negative numbers.")
        

main()
