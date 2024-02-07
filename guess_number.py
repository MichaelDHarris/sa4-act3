
number = 10
print("I'm thinking of a number...")
guess = ''
while guess != 'q' and guess != str(number):
    guess = input("What number am I thinking of? ")
    if guess == 'q':
        print(f"The number was {number}.")
    elif guess == str(number):
        print("Congratulations! You guessed the right number.")
    elif int(guess) > number:
        print("Sorry! That wasn't correct, try going lower!")
    else: print("Sorry! That wasn't correct, try going higher!")
