print("Tip Calculator")
print()
myBill = float(input("What was the bill?: "))
print()
numberOfPeople = int(input("How many people?: "))
print()
tip = int(input("What percentage tip would you like to leave: 15, 18, or 20 percent? "))
cost = myBill / 100
finalTip = cost * tip
billWithTip = finalTip + myBill
billPerPerson = billWithTip / numberOfPeople
answer = round(billPerPerson, 2)
print("You all owe", billPerPerson)
