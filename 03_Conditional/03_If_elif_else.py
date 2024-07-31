#If elif 
"""
Syntax 
if Condition:           if condition 1 is true then it will not check any other condition 
    Code
    Code
    Code
elif Condition:
    Code
    Code
    Code
else :          else is not compulsary 
    Code 
    Code 
    Code


"""


#Ask 2 number from user and print which is greatest

num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))

if num1>num2:
    print("Num 1 is greater.")
elif num2>num1:
    print("Num 2 is greater.")
else:
    print("Both numbers are equal.")


#Question 2 

subj1 = int(input("Enter the marks of Subject 1 : "))
subj2 = int(input("Enter the marks of Subject 2 : "))
subj3 = int(input("Enter the marks of Subject 3 : "))
subj4 = int(input("Enter the marks of Subject 4 : "))
subj5 = int(input("Enter the marks of Subject 5 : "))

percent = (subj1+subj2+subj3+subj4+subj5)/5

if 100 > percent > 90:
    print("A Grade")
elif 90 > percent > 80:
    print("B Grade")
elif 80 > percent > 70:
    print("C Grade")
elif 70 > percent > 60:
    print("D Grade")
elif 0 < percent < 61:
    print("Fail")
else :
    print("INVALID")
