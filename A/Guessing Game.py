#WAP to Guess the Number in 3 Attepmts :
secret_num = 8
guess_Count = 0
guess_limit = 3
while guess_Count < guess_limit:
    guess = int(input('Guess: '))
    guess_Count += 1
    if guess == secret_num:
        print('You Won !!')
        break
else:
    print('Sorry You Failed !!')

