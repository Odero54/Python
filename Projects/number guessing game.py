# importing module
import random
import math

# Asking user to input lower
# and upper bounds
Lower = int(input("Enter the lower bound:- "))
Upper = int(input("Enter the upper bound:- "))

# Compiler select random number between
# upper and lower bound
x = random.randint(Lower, Upper)
print(f"""You've only {round(math.log(Upper - Lower + 1, 2))}
chances to guess the integer!""")

# Initializing the number of guesses
Count = 0
# initialize while loop for
# calculation of
# number of minimum guesses between
# the range (Lower, Upper)
while Count < round(math.log(Upper - Lower + 1, 2)):
    Count += 1
    # Taking guessing number as input
    guess = int(input("Guess a number:- "))
    # Condition testing
    if x == guess:
        print(f"""Congratulations! You did it in
{Count} trials""")
        # Once guessed correctly the loop will break
        break
    elif x < guess:
        print("Try Again! You guessed too high")
    elif x > guess:
        print("Try Again! You guessed too small")
    # If guessing is more than number of guesses
    # print the following output
    if Count >= round(math.log(Upper - Lower + 1, 2)):
        print("Better luck! Next time...")