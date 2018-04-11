# import required function from the random module
from random import randrange 
from random import randint 

# define parameters ahead, so that they can be switched any time later on
range_start = 1
range_finish = 100
max_tries = 10

# create a random integer within the range
secret_number = randint(range_start, range_finish) 

# define the required variables 
guess = -1
counter = 0

# run a loop and let the user guess away
while(secret_number != guess):
    
    print("Guess a number!")
    guess = int(input("Your guess: "))
    
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
