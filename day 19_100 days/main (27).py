print("Loan Calculator")
print()
print("$1000 over 10 years at a 5% interest rate per annum")
print()
total = 1000
for counter in range(10):
  total += (total * 0.05)
  print("Year",counter+1,"is",round(total, 2))
print()
print("You paid",round(total-1000,2),"in interest!")
