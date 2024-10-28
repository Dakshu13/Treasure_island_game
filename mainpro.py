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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# The guessing game application is built on the concept of conditional statements and operators
#Provide the print statement to welcome the viewers on the application
print("Welcome to the treasure world.")
print("Your mission is to find the treasure.")
#Now ask the user whether the person wants to move in left or right direction
ask_direction = input("Type the direction:\n")
#if the user type right, it's game over. Else , ask the user to whether to swim or wait
if ask_direction == "left".lower():
    ask_action = input("Type, whether you wanna swim or wait:\n")
    ##if the user type swim, it's game over else..ask the user to choose the color!
    if ask_action == "Wait".lower():
        color_of_the_door = input("Enter, which color of the door you wanna enter:\n")
        if color_of_the_door == "Yellow".lower():
            print("You Win!")
        elif color_of_the_door == "Red".lower():
            print("Burned by fire.Game over!")
        elif color_of_the_door == "Yellow".lower():
            print("Game over!")
    else:
        print("Game over!")
else:
    print("Game over!")
print("Thanks for playing the game!")