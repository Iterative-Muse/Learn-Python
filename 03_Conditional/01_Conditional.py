# IF Statement : 
'''
Syntax
if condition: {Condition Value output must be True/False}
    code  {Here the 4 space between starting to code and it is known as Indentation }
    code
    code
else:
    code
    code
    code
'''
age =int(input("Enter age = "))
if age >=18:
    print("You can Vote") 
else:
    print("You cannot Vote")
print("Done")

#WAP to print the greatest number 
num1 = int(input("Enter 1 no. = "))
num2 = int(input("Enter 2 no. = "))

if num1 > num2:
    print(f"{num1} is the greatest number.")

else:
    print(f"{num2} is the greatest number.")

#WAP to print the number is odd or even

num1 = int(input("Enter the Number = "))

if num1 % 2 == 0:
    print(f"{num1} is an Even Number")

else:
    print(f"{num1} is an Odd Number")


#WAP to get result pass or fail

physics = int(input("Enter the Physics Marks = "))
chemistry = int(input("Enter the Chemistry Marks = "))

if physics > 35 and chemistry > 35:
    print("Pass !!")
else:
    print("Fail...")
