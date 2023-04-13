import random
passw=''
passw1=''
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']
n=int(input("how many letters do you want to add-->"))
n1=int(input("how many symbols-->"))
n2=int(input("how many numbers-->"))
for char in range(1,n+1):
    passw+=random.choice(letters)
for char in range(1,n1+1):
    passw+=random.choice(symbols)
for char in range(1,n2+1):
    passw+=str(random.randint(0,9))
print(passw)

