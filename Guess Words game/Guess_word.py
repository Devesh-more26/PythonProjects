import random

print('What is you name?', end='')
name = input()
chance = 12
print('Good luck!',name, 'you have',+ chance,'guesses')

words =['happy','geeks','ashish','family','coding','python','money','goodluck','travel']

word = random.choice(words)
guesses = ''

while chance > 0:
    failed = 0
    for i in word:
        if i in guesses:
            print(i)
        else:
            print('_')
            failed += 1
    
    if failed == 0:
        print('You win')
        print('the word is',word)
        break

    print()
    guess = input('guess a character : ')

    guesses += guess

    if guess not in word:
        chance -= 1
        print('Worng')
        print('You have', chance,'more guesses')

        if chance == 0:
            print('You loose')