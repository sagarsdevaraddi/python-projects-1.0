print('''ascii art
''')
print("Welcome to treasure island")
print("your mission is to find treasue.")
choice = input('you\'re at a crossroad,where you want to go? type "left" or "right".').lower()
if choice == "left":
    choice=input('you\'ve come to lake. Type "wait" to wait for the boat. type "swim" to swim across.').lower()
    if(choice=="wait"):
            choice2=input("you arrived to island unharmed. There is a house with 3 doors REd,YEllow and Blue. choose a door").lower()
            if choice2=="red":
                      print("gunshot dead\n game over")
            elif choice2=="yellow":
                      print("alien attack . game over")
            elif choice2=="blue":
                       print("Treasure is yours")
    elif (choice=="swim"):
          print("lost in lake")

else:
    print("you fell into trap hole\nGAME OVER")