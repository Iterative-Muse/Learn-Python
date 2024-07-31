
# Q23. Write a Python program that takes an integer input and prints whether it's positive, negative. (Consider 0 as positive)

num1 = int(input("Enter the Number = "))

if num1 >= 0:
    print(f"Entered number {num1} is Positive.")
else :
    print(f"Entered number {num1} is Negative.")

# Q24. Write a program that takes a character as input and prints whether it's a vowel or a consonant. (Multiple OR will be used)

letter = input("Enter the Alphabet = ")

if letter == "a" or letter == "e" or letter == "i" or letter =="o" or letter == "u" :
    print(f"Letter {letter} is a Vowel.")
else:
    print(f"Letter {letter} is consonant")


# Q25. Write a program that takes two numbers as input and checks if the first number is divisible by the second.

num1 = int(input("Enter Number 1 = "))
num2 = int(input("Enter Number 2 = "))

if num1%num2 == 0:
    print(f"The Number {num1} is divisible by {num2}.")
else:
    print(f"The Number {num1} is not divisible by {num2}.")

# Q26. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.

# 1. Print percentage of class attended
# 2. Print Is student is allowed to sit in exam or not.

total_class = int(input("Enter the total Number of classes held : "))
attend_class = int(input("Enter the number of attended classes : "))

percentage = (attend_class/total_class)*100
print(f"Percentage of class attended = {percentage}%")
if percentage > 75:
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam")


