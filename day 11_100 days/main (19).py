print ("Seconds in a Year")
print()
year = int(input("What year is it?: "))
minute = (60)
hour = (60 * minute)
day = (24 * hour)
annual = (365 * day)
leapYear = (year % 4)
if leapYear % 4 == 0:
  print ("There are ",annual + day,"seconds in the year",year)
else:
  print ("There are ",annual,"seconds in the year",year)
