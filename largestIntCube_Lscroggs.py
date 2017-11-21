#largestIntCube
#Checking for the largest int cubed < 12000
#Lawrence Scroggs
#Python 3.6.2
import math
def main():
    product = 0
    x = 0
    y = 0
    while product < 12000:
        print(product)
        y = x + 1
        y = y * y * y
        if y < 12000:
            x += 1
            product = x * x * x
        else:
            break


    print("The largest integer that is less than 12000 while cubed is",x,'.')

main()
