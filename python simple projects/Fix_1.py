#Accept the name
import random
a=1
print("Do you accept mistakes and comprimise? then type 1\n")
if(int(input())==1):
    for i in range(0, 999):
        a = input("Enter a name with space between each letter ex:s a g a r\n").lower()
        b = a.split(" ")
        d = len(b)
        sd=''
        v=sd.join(b)
        b[random.randint(0, d - 1)] = 'u'
        b = sd.join(b)
        print(f"{b} Is the name correct,if no please choose:1-re-enter 2-ok it is acceptable")
        o = int(input())
        if o == 1:
            continue
        else:
           exit("Hello"+" "+v)






