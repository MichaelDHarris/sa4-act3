
number = 10
print("I'm thinking of a number...")
guess = ''
while guess != 'q' and guess != str(number):
    guess = input("What number am I thinking of? ")
    if guess == 'q':
        print(f"The number was {number}.")
    elif guess == str(number):
        print("Congratulations! You guessed the right number.")
    else:
        print(f"Sorry! The number was {number}! Try again.")
