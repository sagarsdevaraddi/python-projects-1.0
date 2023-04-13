import random

print("welcome to East-Head Lottery\nCredit your Lottery account with money than play\n1-time cost ₹25,10-times cost ₹200,15-times cost ₹275\nWinner gets ₹2000\nTax of 10% on winning amount greater than ₹10,000")
pay=int(input("Enter amount to be credited-->"))
if(pay>=50):
    a = int(input("choose:1-one time,2-10 times,3-15 times-->"))

    if a == 1:

        b = int(input("choose your lucky number of two digits: example--> 07-->"))
        if b == random.randint(0, 99):
            pay += 2000
            print("congratulations you have won ₹2000 ")

        else:
            print(f"Try one more time\nyour account balance=₹{pay - 25}")
            if pay < 0:
                print(f"please pay the Bill {pay}")
    elif (a == 2 and pay>=200):
        pay-=200
        for i in range(0, 10):
            b = int(input("choose your lucky number of two digits: example--> 07-->"))
            if b == random.randint(0, 99):
                pay += 2000
                continue
        if pay > 10000:
            pay = (pay * 0.1) - pay

        print(f"congratulations you won ₹{pay}\nThank you for playing")
        if pay<0:
            print(f"please pay the Bill {pay}")
    elif (a == 3 and pay>=275):
        pay-=275
        for i in range(0, 15):
            b = int(input("choose your lucky number of two digits: example--> 07-->"))
            if b == random.randint(0, 99):
                pay += 2000
                continue
        if pay > 10000:
            pay = (pay * 0.1) - pay
        print(f"congratulations you won ₹{pay}\nThank you for playing")
        if pay<0:
            print(f"please pay the Bill {pay}")
    else:
        print(f"Choose the given options only(1,2,3) or add more money to play this game")


else:
    print("Please deposit minimum of ₹50 to play")