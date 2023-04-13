import random
passw=[]
p=''
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']
numbers=['1','2','3','4','5','6','7','8','9']
choic=int(input("input the password length-->"))
for char in range(1,choic+1):
       p+=random.choice(letters+symbols+numbers)
print(p)
# for i in range(0,len(p)):
#
# print(f"suggested password is:{p1}")