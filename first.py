#rock-paper-scissor game

import random

choices =["rock","paper","scissor"]

def userchoice():
    user = input("Enter your choice(rock,paper,scissor):").lower()
    while user not in choices:
        print("Invalid input!!!!")
        user = input("Enter your choice(rock,paper,scissor):").lower()
    return user

def computerchoice():
    computer = random.choice(choices)
    return computer

    

def play():
    user = userchoice()
    computer = computerchoice()
    print(computer)
    if user == computer:
        print("It was a tie!!!")
    elif((user=="rock" and computer=="scissor") or (user == "paper" and computer =="rock")or(user=="scissor" and computer=="paper")):
        print("Congratulations,You won the game!!!!")
    else:
        print("OOPS!!!You lost the game...Try again..") 
    
play()

    

while(True):
    oncemore = input("Do you want to give another try(yes/no):").lower()
    if oncemore == 'yes':
        play()
    elif oncemore=="no":
        print("********GAME COMPLETED***********")
        break
    else:
        print("Enter a valid input")
    