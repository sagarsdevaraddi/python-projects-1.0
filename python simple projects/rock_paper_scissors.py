#Rock paper and scissors Game
import random
rock ='''✊✊✊✊✊✊✊'''
paper='''✋✋✋✋✋✋✋'''
scissors = '''✌️✌️✌️✌️✌️'''
print("Welcome to rock,paper and scissors game")
choice_1 = input("choose rock or paper or scissors ").lower()
print(f"your choice is {choice_1}")
if(choice_1=="rock"):
    print(rock)
elif(choice_1=="paper"):
    print(paper)
elif(choice_1=="scissors"):
    print(scissors)
else:
    print("choose only one rock,paper or scissors")
l = ["rock","paper","scissors"]
d = len(l)
random_choice = random.randint(0,d-1)
sed = l[random_choice]
print(f"computer chose {sed}")
if(sed=="rock"):
    print(rock)
elif(sed=="paper"):
    print(paper)
elif(sed=="scissors"):
    print(scissors)

if(sed==choice_1):
    print("No one won. it's a Draw")
elif(sed=="rock" and choice_1=="paper"):
    print("you won")
elif(sed=="rock" and choice_1=="scissors"):
    print("you lose")
elif(choice_1=="rock" and sed=="paper"):
    print("you lose")
elif(choice_1=="rock" and sed=="scissors"):
    print("you won")
elif(choice_1=="paper" and sed=="scissors"):
    print("you lose")
elif(choice_1=="scissors" and sed=="paper"):
    print("you won")
print("Thank you for playing GG")


