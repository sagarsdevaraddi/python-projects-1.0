#Roller coster TicketBilling
print("Welcome to rollercoster")
print("Here is the ticket prices\n"
      "₹150 for age 13 to 18\n"
      "₹200 for age 18+ ")
pay = int(input("Enter your age\n"))
if(12<pay<=65):
    pay2=150*int(input("how many tickets of ₹150 you want\n"))
    pay3=200*int(input("how many tickets of ₹200 you want\n"))
    Total_Bill = pay2 + pay3
    if(Total_Bill>=1200):
        Total_Bill=Total_Bill-Total_Bill*0.1
    print(f"Your total bill is ₹{Total_Bill}\nplease verify your age with Aadhar card at ticket checking")
else:
    current=(13*365)-(pay*365)
    print(f"sorry you are too young to play,come after {current} Days later")