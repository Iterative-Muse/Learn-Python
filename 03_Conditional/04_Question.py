
# Q1. Write a program to check if the number is ODD, EVEN or Equal to Zero.

num = int(input("Enter Number 1 :"))
if num == 0:
    print("Number is Equal to Zero")
elif num % 2 == 0:
    print("Entered Number is Even")
elif num % 2 != 0:
    print("Entered Number is Odd")

# Q2. Write a program to check if number is divisible by 2 and 3 but not 8.
num = int(input("Enter Number : "))

if num % 2 == 0 and num % 3 == 0 and num % 8 != 0:
    print("Enter Number is Divisible by 2 and 3 but not 8.")

else :
    print("Enter number is divisable by 2,3,8")

# Q3. Write a program to print the last digit of a number
num = int(input("Enter a Number : "))

last_digit = num % 10

print(f"Last Digit of the entered number {num} is {last_digit}")

# Q4. Write a program to check if the last digit of a number is divisible by 5 or not.

num = int(input("Enter the Number :"))

last_digit = num % 10

if last_digit == 5 or last_digit == 0:
    print("Given Number is Divisible by 5.")

else :
    print("Given Number is not Divisible by 5.")

# Q5. Write a program to calculate bill. Ask the final amount from the user.
# You have to give discount and print the final bill after discount.
# 50000 above - 30% discount
# 40000 - 49999 - 25% discount
# 30000 - 39999 - 20% discount
# 10000 - 29999 - 10% discount
# 1 - 9999 - No discount
# Print the discount and the final amount to be paid.

final_price = int(input("Enter the Final Amount = "))

if final_price >= 50000:
    discount = (final_price * 30) / 100
    discount_price = final_price - discount
    print(f"Final Price after discount of 30% is Rs. {discount_price}")
elif final_price <= 49999 and final_price >= 40000:
    discount = (final_price * 25) / 100
    discount_price = final_price - discount
    print(f"Final Price after discount of 25% is Rs. {discount_price}")
elif final_price <= 39999 and final_price >= 30000:
    discount = (final_price * 20) / 100
    discount_price = final_price - discount
    print(f"Final Price after discount of 20% is Rs. {discount_price}")
elif final_price <= 29999 and final_price >= 10000:
    discount = (final_price * 10) / 100
    discount_price = final_price - discount
    print(f"Final Price after discount of 10% is Rs. {discount_price}")
else :
    print(f"Sorry there is no discount. Amount = {final_price}")

# Q6. Ask 4 numbers from user. Make sure all the numbers entered by user are different. Print which number is the smallest.

num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
num3 = int(input("Enter the number 3 : "))
num4 = int(input("Enter the number 4 : "))

if num1 != num2 != num3 != num4:
    if num1 < num2 and num1 < num3 and num1 < num4:
        print(f"First Number {num1} is smallest")
    elif num2 < num3 and num2 < num4:
        print(f"Second Number {num2} is smallest")
    elif num3 < num4:
        print(f"Third Number {num3} is smallest")
    else:
        print(f"Fourth Number {num4} is Smallest")
else :
    print("Enter Number is repeated !!")

# Q7. Ask a Number from user.
# Print “Fizz” if the number is divisible by 3.
# Print “Buzz” if the number is divisible by 5.
# Print “FizzBuzz” if the number is divisible by 3 and 5.
# Print the number itself if none of the conditions are true.

num = int(input("Enter The Number : "))

if num % 3 == 0 and num % 5 != 0:
    print("Fizz")
elif num % 3 != 0 and num % 5 == 0:
    print("Buzz")
elif num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
else:
    print(num)




