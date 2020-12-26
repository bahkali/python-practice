# import random

def guessNumber (num1, num2):
    while True: 
        #ask the number
        guess = int(input(f'Please enter a random number between {num1} ~ {num2}: '))
        #condition if found
        if num1 < guess < num2:
            print('You are a genius!')
            break
        #condition if not found
        else: 
            print(f'wrong try again number between {num1} ~ {num2}...')
    