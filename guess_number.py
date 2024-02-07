
number = 10
print("I'm thinking of a number...")
numguess = 0
capguess = 3
guess = ''
while guess != 'q' and guess != str(number) and numguess != capguess:
    guess = input("What number am I thinking of? ")
    if guess == 'q':
        print(f"The number was {number}.")
    elif guess == str(number):
        print("Congratulations! You guessed the right number.")
    else:
        numguess += 1
        print(f"Sorry! The number was {number}! You have {capguess - numguess} guess(es) left.")
