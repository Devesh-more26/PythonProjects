import random

print('This is a number guessing game ')
print('You will have only 7 chances to guess the right number')

target = random.randrange(100)
chance = 7

while chance > 0 :
    print('Enter your guess = ', end="")
    guess = int(input())

    if guess == target and chance > 0:
        print('Congratulation, You have guessed the right number')
        break
    elif guess > target :
        print('You have guess too higher')
    elif guess < target :
        print('You have guess too lower')

    chance = chance - 1

    if chance == 0:
        print('Sorry, You have lose the game')
        

