def Play():
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

    choice1 = input('You\'re at a cross road. Where do you want to go? Type "l" or "r" \n').lower()
    if choice1 == "l":
      choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "w" to wait for a boat. Type "s" to swim across. \n').lower()
      if choice2 == "w":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red 'r', one yellow 'y' and one blue 'b'. Which colour do you choose? \n").lower()
        if choice3 == "r":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "y":
         print("You found the treasure! You Win!")
         again=input("Try again?y/n")

        elif choice3 == "b":
         print("You enter a room of beasts. Game Over.")
         again=input("Try again?y/n")

        else:
         print("You chose a door that doesn't exist. Game Over.")
        again=input("Try again?y/n")

      else:
            print("You get attacked by an angry trout. Game Over.")
            again=input("Try again?y/n")

    else:
      print("You fell into a hole. Game Over.")
    retry=input("Do you wish to retry?y/n")
    if retry=="y":
        Play()
    else:
        quit()    
Play()      