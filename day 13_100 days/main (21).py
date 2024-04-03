testName = input("Name of test: ")
maxScore = int(input("Max. possible score: "))
pointsReceived = int(input("Score received: "))
onePercent = pointsReceived / maxScore
percentage = onePercent * 100
answer =  round(percentage, 2)

if answer >= 90 and answer <= 100:
  print ("You have scored", "\033[34m",answer,"%","\033[0m","on your", testName, "test!")
  print("Keep up the hard work!")
  print()
  print ("This means you got an","\033[34m","A+","\033[0m","!")
  
elif answer >= 80 and answer <= 89:
  print ("You have scored", "\033[36m",answer,"%","\033[0m","on your", testName, "test!")
  print("Good job!")
  print()
  print ("This means you got an","\033[36m","A","\033[0m","!")

elif answer >= 70 and answer <= 79:
  print ("You have scored", "\033[32m",answer,"%","\033[0m","on your", testName, "test!")
  print("Not bad!")
  print()
  print ("This means you got a", "\033[32m", "B","\033[0m", "!")

elif answer >= 60 and answer <= 69:
  print("You have scored", "\033[33m",answer,"%","\033[0m","on your", testName, "test!") 
  print()
  print ("This means you got a", "\033[33m", "C","\033[0m", "!")
  print()
  print("On the bright side, at least you passed!")

elif answer >= 50 and answer < 59:
  print("You have scored", "\033[31m",answer,"%","\033[0m","on your", testName, "test!") 
  print()
  print ("This means you got a", "\033[31m", "D","\033[0m", "!")
  print()
  print("Time to find a tutor!")

else:
  print("You have scored", "\033[30m",answer,"%","\033[0m","on your", testName, "test!")
  print()
  print ("This means you got a", "\033[30m", "U","\033[0m", "!")
  print()
  print("Oh no, you're on the verge of failing this class! Time to find a tutor - and fast!")

 #Add colour to text: 
#print("\033[0m") - default
#print("\033[30m") - black
#print("\033[31m") - red
#print("\033[32m") - green
#print("\033[33m") - yellow
#print("\033[34m") - blue
#print("\033[35m") - purple
#print("\033[36m") - cyan
#print("\033[37m") - white
