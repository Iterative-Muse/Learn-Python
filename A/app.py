# #WAP to print the value of John Smith
# name = 'John Smith'
# age = 20
# new_patient = True
#
# print('Name :',name)
# print('Age :' ,age)
# print("New Patient :" ,new_patient)


# #WAP to get the input like their name and fav color and print it
# name = input('What is your name? ')
# fav_color = input('What is your favourite Color? ')
# print(name + " likes " + fav_color)


# #WAP to calculate your age using your birth year
# birth_year =int (input('What is your Birth Year : '))
# age = 2023 - birth_year
# print(age)
# #OR
# birth_year =input('What is your Birth Year : ')
# age = 2023 - int(birth_year)
# print(age)


# #WAP to get the user weight into pounds and convert it into KG.
# pounds = input('Weight in Pounds :')
# kg = float(pounds)/ 2.20462262
# print("Your Weight in KG : ", int(kg))

# #WAP to print multiple lines in Single Print function.
# print('''
# Hello Team,
# Greetings!!
#       I am Tushar Mandali
#       I am 22 Years old
# Regards
# Tushar Mandali''')


# #Fun Activity
# name = 'Jennefer'
# print(name[1:-1])


# #Formatting String
# first = 'John'
# last = 'Smith'
# message = first + " [" + last + "] is a coder"
# msg = (f'{first} [{last}] is a coder.')  # It is formating string which is easy to visualize the sentence for others
# print(msg)


# #To calculate the characters present in a String Sentence
# sentence = 'My name is Tushar Mandali'
# print(len(sentence)) #We use builtin function len() to see the number


# #Methods
# course = 'Hello Everyone, I am Tushar'
# print(course.upper())           # It will change all the uppercase letter into upper case
# print(course.lower())           # It will change all the lowercase letter into upper case
# print(course.find('o'))         # It is used to find the char in which position it is. It is a case sensitive method
# print(course.find('Z'))         # If the char is not exist in the string it will return "-1" as an output
# print(course.replace('Everyone','Team'))    # It is used to replace things into new ones.
# print('Tushar' in course)       # It is used to check the word or string exist in the variables or not in Bollean form


# #Arithmetic Operators
# print(10 + 2)
# print(10.33 - 2)
# print(10 * 3)                       # MULTIPLICATION
# print(10 / 3)                       # to get divide answer
# print(10 % 3)                       # to get reminder
# print(10 ** 3)                      # It is used to give power to a number like "10" to the power "3"


# #Augmented or Enhanced Assignment Operator
# x = 10
# x += 5                  #ADDITION
# print(x)
# x = 10
# x -= 5                  #SUBSTRACT
# print(x)
# x = 10
# x /= 5                  #DIVIDE
# print(x)
# x = 10
# x %= 5                  #MODULO
# print(x)
# x = 10
# x *= 5                  #MULTIPLICATION
# print(x)
# x = 10
# x **= 5                 #TO THE POWER "5"
# print(x)


# #Operator Presendence
# Paranthasis ()
# Exponentiation 2 ** 3
# Multiplication or Division
# Addition or Substraction

# import math
# print(math.ceil(2.9))
# print(math.floor(2.9))

# #WAP using if else statement
# house_price = 1000000
# down_payment = 0
# credit_good = False
# if  credit_good:
#     down_payment = (house_price/100) * 10
# else:
#     down_payment = (house_price / 100) * 20
# print(f'Down Payment : ${down_payment}')


# #WAP to get the validation error
# name = input("What is your Name? ")
# num_char = len(name)            #Take the number of char in a variable
# if num_char < 3:               #comparing that variable as per the condition
#     print("Name must be at least 3 Characters !!")
# elif num_char > 50:
#     print("Name can be a Maximum of 50 Characters !!")
# else:
#     print("Name looks good !!")

# #Logical Operator
# if var1 and var2:
# if var1 or var2:
# if var1 and not var2:
# if var1 or not var2:


# #Comparison Operator:
# name = input("What is your Name? ")
# num_char = len(name)            #Take the number of char in a variable
# if num_char < 3:               #comparing that variable as per the condition
#     print("Name must be at least 3 Characters !!")
# elif num_char > 50:
#     print("Name can be a Maximum of 50 Characters !!")
# else:
#     print("Name looks good !!")


# #While Loop:
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("Done !!")

# #For Loop :
# for item in "Tushar":
#     print(item)

# for item in [1,2,3,4,5,6]:
#     print(item)

# for item in range(1 , 10 , 2):    #starts from 1 to 10 and 2 is used to move 2 numbers ahead. like 1,3,5,7 to 9
#     print(item)

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f'Total: {total}')


# #Nested Loops
# for x in range(4):
#     for y in range(3):
#         print(f"({x} , {y})")

# #WAP to print F using  nesting loop
# numbers = [5, 2, 5, 2, 2]
# for number in numbers:
#     output = ''
#     for num in range(number):
#         output += 'x'
#     print(output)


#Lists






