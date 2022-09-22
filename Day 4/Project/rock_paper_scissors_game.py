# Make a rock, paper, scissors game.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input <= -1 or user_input > 2:
    exit("Wrong Input.\nTry again!")

if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
else:
    print(scissors)

print()
print("Computer choose:\n")
computer_input = random.randint(0, 2)
if computer_input == 0:
    print(rock)
elif computer_input == 1:
    print(paper)
else:
    print(scissors)

result = ""
if user_input == computer_input:
    result = "Draw!"
elif user_input == 0:
    if computer_input == 1:
        result = "You Lose!"
    else:
        result = "You Win!"
elif user_input == 1:
    if computer_input == 0:
        result = "You Win!"
    else:
        result = "You Lose!"
elif user_input == 2:
    if computer_input == 0:
        result = "You Lose!"
    else:
        result = "You Win!"

print(result)
