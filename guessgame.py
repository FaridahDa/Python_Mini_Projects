from random import randint

n = randint(1,30)

guess_count = 1

guess_limit = 3

print("-------------------------------------")
print("WELCOME TO THE GUESSING GAME")
print("-------------------------------------")

while guess_count <= guess_limit:
    guess = int(input("Please enter your guess:"))
    guess_count += 1


    if guess < n:
        print("Your guess is too LOW!, Try again!")
    elif guess > n:
        print("Your Guess is too HIGH! Try again!")
    elif guess == n:
        print(f"Your Guess is correct, yes the correct number is {n}")




