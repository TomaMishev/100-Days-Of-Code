# Make your own "Choose Your Own Adventure" game.
# Use conditionals such as `if`, `else`, and `elif` statements to lay
# out the logic and the story's path in your program.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

cross_command = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if cross_command == 'left':
    wait_command = input(
        'You\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type '
        '"swim" to swim across.\n').lower()
    if wait_command == 'wait':
        door_choice_command = input(
            "You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. "
            "Which colour do you choose?\n").lower()
        if door_choice_command == 'red':
            print("It's a room full of fire.\nGame Over.")
        elif door_choice_command == 'blue':
            print("You enter a room of beasts.\nGame Over.")
        elif door_choice_command == 'yellow':
            print("You found the treasure!\nYou Win!")
        else:
            "You chose a door that doesn't exist.\nGame Over."
    else:
        print("You get attacked by an angry trout.\nGame Over.")
else:
    print("You fell into a hole.\nGame Over.")
