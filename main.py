##-----------Rock Paper Scissors Game----------##
##-----------You Vs Computer----------##
#Rules for playing the Game
'''The game is played with three possible hand signals that represent a rock, paper, and scissors. The rock is a closed fist; paper is a flat hand with fingers and thumb extended and the palm facing downward; and scissors is a fist with the index and middle fingers fully extended toward the opposing player. Rock wins against scissors; paper wins against rock; and scissors wins against paper. If both players throw the same hand signal, it is considered a tie and play resumes until there is a clear winner.'''
import random
def game(pc,you):
    if pc==you:
        return None
    elif pc=='r':
        if you=='s':
            return False
        elif you== 'p':
            return True
    elif pc=='p':
        if you=='r':
            return False
        elif you== 's':
            return True
    elif pc=='s':
        if you=='p':
            return False
        elif you== 'r':
            return True

print("Computer Turn: Rock(r) Paper(p) Or Scissors(s)?")
#generating random number using random module, which produces random number between two integers
randNum= random.randint(1,3)
#if random number generated by pc is 1. Then choice of pc will be Rock
if randNum ==1:
    pc='r'
#if random number generated by pc is 2. Then choice of pc will be Paper
elif randNum ==2:
    pc='p'  
#if random number generated by pc is 3. Then choice of pc will be Scissors
elif randNum ==3:
    pc='s'  

#Now it's the players turn to pick one choice from Rock Paper Or Scissors.
you=input("Your Turn: Rock(r) Paper(p) Or Scissors(s)?\n")

playGame=game(pc,you)

print(f"Computer chose {pc}")
print(f"You chose {you}")

if playGame==None:
    print("The game is a Tie!!\nPlay again!!")
elif playGame:
    print("You win!!")
else:
    print("You Lose!!")