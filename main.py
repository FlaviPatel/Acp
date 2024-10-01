import random

n = random.randrange(51, 89)

guess = int(input("Enter the number:"))
while n != guess:
    if guess < n:
        print("Too Low")
        guess = int(input(" Enter a number again:"))
    elif guess > n:
        print("Too High")
        guess = int(input(" Enter a number again:"))
    else:
        print("you guessed it right!")

print("Congratulations on winning the game !!")
    