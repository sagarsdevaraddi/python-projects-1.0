year = int(input("Which year you want to check it is leap year or not "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
             print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")

    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")