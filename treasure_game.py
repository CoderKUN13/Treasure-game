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


decison1 = input("You are on an island and you see a cave but there is a river in the way. Do you want to wait for a boat or swim accross? Choose 'swim' or 'wait' ").lower()

if decison1 == "swim":
  print("You swam accross the river and found three doors: 1.Red 2.Blue 3.Yellow")
  decison2 = input("Which door do you want to pick? red, blue or yellow?").lower()
  if decison2 == "red":
    print("You enter a room of lions and you die....GAME OVER :(")
  elif decison2 == "blue":
    print("You enter a room of snakes and you die....GAME OVER :(")
  elif decison2 == "yellow":
    print("You enter a room of hot naked horny women.....YOU WIN!!!")
else:
  print("You wait and a Pirate boat arrives and kills you....GAME OVER :(")
  


