from random import randrange 
from random import randint 

def input_and_verify():
    print("Guess a number!")
    while True:
        try:
            number = int(input("Your guess: "))
            if number > 0:
                return number
                break
            else:
                print("That's not a positive integer. Try again.")
        except ValueError:
            print("That's not a number. Try again.")
    
range_start = 1
range_finish = 100
max_tries = 10

secret_number = randint(range_start, range_finish) 

guess = -1
counter = 0

while(secret_number != guess):
    
    guess = input_and_verify()

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Right on!")
        
    counter = counter + 1
    
    if(counter == max_tries):
        print("No more tries allowed.")
        break
