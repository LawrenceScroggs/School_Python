#File:student_LScroggs.py
#Description: Finding out if a student is in CS160
#Author: Lawrence Scroggs
#Date: 10/15/17
#Compiler: Python 3.6.2
#While testing could not figure out how to exclude integers as invalid
#forgot to add exit
print("SEARCH FOR A STUDENT""\n\n")
student = input("What is the first and last name of the student you are looking for? ")
student = student.lower()
print('')
print("Class List:\nJames Mcree\nAna Amari\nGenji Shimada\nLena Oxton\n\n")
if student == "james mccree":
    print("James McCree is in the class.")
elif student == "ana amari":
    print("Ana Amari is in the class.")
elif student == "genji shimada":
    print("Genji Shimada is in the class.")
elif student == "lena oxton":
    print("Lena Oxton is in the class.")
else:
    print('',student,"is not in the class. Sorry.")
    exit()
    
    
