#split
import random

name_string = input("Give me everbody's names separated by commma-->")
name = name_string.split(",")

x=len(name)

y=random.randint(0,x-1)
print(f"{name[y]} is going to buy the meal today")
