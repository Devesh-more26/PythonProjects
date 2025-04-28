import time
import random

print("Rock Paper Scissor Game")
print()

a = input("Enter Name :")
b = input("Enter Age :")
c = input("Maturity Level :")
print()

print("Saving data....")
time.sleep(4)
print("data saved")

print("--- Game Rules ---")
print("Rock vs paper-> paper wins")
print("Rock vs scissor-> Rock wins")
print("paper vs scissor-> scissor wins")
print()

choices = ['paper','rock','scissor']

print("Start the game!!")
print()
print('You only have 5 turns to win the game')


count = 0
i=0
while (i < 5):
    user = input("Enter your hand :")
    comp = random.choice(choices)

    if user == 'rock' and comp == 'scissor':
        print(a.upper()," WINS")
        count = count + 1
    elif user == 'rock' and comp == 'paper':
        print(a.upper()," loose")
        count = count - 1
    elif user == 'rock' and comp == 'rock':
        print("Match Draw")
    elif user == 'paper' and comp == 'rock':
        print(a.upper()," WINS")
        count = count + 1
    elif user == 'paper' and comp == 'paper':
        print("Match Draw")
    elif user == 'paper' and comp == 'scissor':
        print(a.upper(),"loose")
        count = count - 1
    elif user == 'scissor' and comp == 'paper':
        print(a.upper()," WINS")
        count = count + 1
    elif user == 'scissor' and comp == 'rock':
        print(a.upper(),"loose")
        count = count - 1
    elif user == 'scissor' and comp == 'scissor':
        print("Match Draw")

    i = i+1

print()
print("Score : ",count)
print()
print("Do you want to play again....")

if count <= 2:
    print("YOU LOSE -- GAME OVER")
elif count > 2 :
    print("YOU WIN THE GAME")
    

