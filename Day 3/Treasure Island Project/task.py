print(r'''
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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road.")

direction=input("Where do you want to go? \nType 'left' or 'right'. \n  ")
right=0
left=0

if direction=="left":
    print("You've come to lake.")
    choice1=input("There is an island in the middle of the lake. \n Type 'wait to wait for a boat.Type 'swim' to swim across.\n")

    wait =0
    swim=0

    if choice1 == "wait":
     print("You arrive at the island unharmed.")
     choice2=input("There is a house with 3 doors.\n One 'red',One 'yellow',One 'blue'.Which color do you choose? \n" )

     blue=0
     red=0
     yellow=0

     if choice2 == "red":
         print("You burned by fire.Game over.")

     elif choice2 == "yellow":
         print("You win!.")

     elif choice2 == "blue":
         print("Eaten by beast.Game over.")

     else:
         print("Game Over.")

    elif choice1 == "swim":
     print("Attacked by trout.Game over.")
    else:
        print("Attacked by trout.Game over.")


elif direction=="right":
    print("You fell into a hole. Game Over.")
else:
    print("Illegal Action")




