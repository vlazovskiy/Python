# guess-a-number-game
A simple game where a user is prompted to guess a number between 1 and 100 and is given a maximum of 10 tries.

Note that V1 script assumes that a user will enter a valid integer. If the input is ivalid, the script will show a standard error message:
> Traceback (most recent call last):
>   File "metis1.py", line 15, in <module>
>     guess = int(input("Your guess: "))
> ValueError: invalid literal for int() with base 10: 'u'
  
V2 has a function which checks input and returns an error message when a non-integer or a negative integer is entered.

Written for Python 3.x.x
