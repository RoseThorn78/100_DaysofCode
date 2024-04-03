#Stops either players from viewing each others input
from getpass import getpass as input

print("ULTIMATE ROCK🪨, PAPER📄, SCISSORS✂️ !")
print()

#round1 input
print("Let ROUND 1 Begin!")
print("Good luck players!")
print()
p1 = input("Player 1, please select your move(R, P or S): ")
p2 = input("Player 2, please select your move(R, P or S): ")
print()

if p1 == "R" or p1 == "r":
  p1Result = "ROCK🪨"
elif p1 == "P" or p1 == "p":
  p1Result = "PAPER📄"
elif p1 == "S" or p1 == "s":
  p1Result = "SCISSORS✂️"
else:
  print("Try again")
  
if p2 == "R" or p2 == "r":
  p2Result = "ROCK🪨"
elif p2 == "P" or p2 == "p":
  p2Result = "PAPER📄"
elif p2 == "S" or p2 == "s":
  p2Result = "SCISSORS✂️"
else:
  print("Try again")

#round1 results
if p1Result == "ROCK🪨" and p2Result == "ROCK🪨":
  print("Both Player 1 and Player 2 picked ROCK🪨!")
  print("It was a tie!")
  round1Results = "TIE"
elif p1Result == "ROCK🪨" and p2Result == "SCISSORS✂️":
  print("Player 1's ROCK🪨 completely obliterated Player 2's SCISSORS✂️!")
  print("Player 1 WINS round 1!!!")
  round1Results = "P1 WIN"
elif p1Result == "ROCK🪨" and p2Result == "PAPER📄":
  print("Yeesh! Player 1's ROCK🪨 was smothered by Player 2's PAPER📄!")
  print("Player 2 WINS round 1!!!")
  round1Results = "P2 WIN"
elif p1Result == "SCISSORS✂️" and p2Result == "ROCK🪨":
  print("Player 2's ROCK🪨 completely obliterated Player 1's SCISSORS✂️!")
  print("Player 2 WINS round 1!!!")  
  round1Results = "P2 WIN"
elif p1Result == "PAPER📄" and p2Result == "ROCK🪨":
  print("Yeesh! Player 2's ROCK🪨 was smothered by Player 1's PAPER📄!")
  print("Player 1 WINS round 1!!!") 
  round1Results = "P1 WIN"
elif p1Result == "PAPER📄" and p2Result == "PAPER📄":
  print("Both Player 1 and Player 2 picked PAPER📄!") 
  print("It was a tie!")
  round1Results = "TIE"
elif p1Result == "PAPER📄" and p2Result == "SCISSORS✂️":
  print("Wow, Player 2's SCISSORS✂️ absolutely shredded Player 1's PAPER📄!")
  print("Player 2 WINS round 1!!!")
  round1Results = "P2 WIN"
elif p1Result == "SCISSORS✂️" and p2Result == "PAPER📄":
  print("Wow, Player 2's SCISSORS✂️ absolutely shredded Player 1's PAPER📄!")
  print("Player 1 WINS round 1!!!")
  round1Results = "P1 WIN"
else:
  print("Both Player 1 and Player 2 picked SCISSORS✂️!") 
  print("It was a tie!")
  round1Results = "TIE"

#round2 input
print()
print("Now for round 2!")
print("Good luck players!")
print()
p1 = input("Player 1, please select your move(R, P or S): ")
p2 = input("Player 2, please select your move(R, P or S): ")
print()

if p1 == "R" or p1 == "r":
  p1Result = "ROCK🪨"
elif p1 == "P" or p1 == "p":
  p1Result = "PAPER📄"
elif p1 == "S" or p1 == "s":
  p1Result = "SCISSORS✂️"
else:
  print("Try again")
  
if p2 == "R" or p2 == "r":
  p2Result = "ROCK🪨"
elif p2 == "P" or p2 == "p":
  p2Result = "PAPER📄"
elif p2 == "S" or p2 == "s":
  p2Result = "SCISSORS✂️"
else:
  print("Try again")

#round2 results
if p1Result == "ROCK🪨" and p2Result == "ROCK🪨":
  print("Both Player 1 and Player 2 picked ROCK🪨!")
  print("It was a tie!")
  round2Results = "TIE"
elif p1Result == "ROCK🪨" and p2Result == "SCISSORS✂️":
  print("Player 1's ROCK🪨 completely obliterated Player 2's SCISSORS✂️!")
  print("Player 1 WINS round 2!!!")
  round2Results = "P1 WIN"
elif p1Result == "ROCK🪨" and p2Result == "PAPER📄":
  print("Yeesh! Player 1's ROCK🪨 was smothered by Player 2's PAPER📄!")
  print("Player 2 WINS round 2!!!")
  round2Results = "P2 WIN"
elif p1Result == "SCISSORS✂️" and p2Result == "ROCK🪨":
  print("Player 2's ROCK🪨 completely obliterated Player 1's SCISSORS✂️!")
  print("Player 2 WINS round 2!!!")  
  round2Results = "P2 WIN"
elif p1Result == "PAPER📄" and p2Result == "ROCK🪨":
  print("Yeesh! Player 2's ROCK🪨 was smothered by Player 1's PAPER📄!")
  print("Player 1 WINS round 2!!!") 
  round2Results = "P1 WIN"
elif p1Result == "PAPER📄" and p2Result == "PAPER📄":
  print("Both Player 1 and Player 2 picked PAPER📄!") 
  print("It was a tie!")
  round2Results = "TIE"
elif p1Result == "PAPER📄" and p2Result == "SCISSORS✂️":
  print("Wow, Player 2's SCISSORS✂️ absolutely shredded Player 1's PAPER📄!")
  print("Player 2 WINS round 2!!!")
  round2Results = "P2 WIN"
elif p1Result == "SCISSORS✂️" and p2Result == "PAPER📄":
  print("Wow, Player 2's SCISSORS✂️ absolutely shredded Player 1's PAPER📄!")
  print("Player 1 WINS round 2!!!")
  round2Results = "P1 WIN"
else:
  print("Both Player 1 and Player 2 picked SCISSORS✂️!") 
  print("It was a tie!")
  round2Results = "TIE"

#round3 input
print()
print("Let's begin the third, and final, round!")
print("Good luck players!")
print()
p1 = input("Player 1, please select your move(R, P or S): ")
p2 = input("Player 2, please select your move(R, P or S): ")
print()

if p1 == "R" or p1 == "r":
  p1Result = "ROCK🪨"
elif p1 == "P" or p1 == "p":
  p1Result = "PAPER📄"
elif p1 == "S" or p1 == "s":
  p1Result = "SCISSORS✂️"
else:
  print("Try again")
  
if p2 == "R" or p2 == "r":
  p2Result = "ROCK🪨"
elif p2 == "P" or p2 == "p":
  p2Result = "PAPER📄"
elif p2 == "S" or p2 == "s":
  p2Result = "SCISSORS✂️"
else:
  print("Try again")

#round3 results
if p1Result == "ROCK🪨" and p2Result == "ROCK🪨":
  print("Both Player 1 and Player 2 picked ROCK🪨!")
  print("It was a tie!")
  round3Results = "TIE"
elif p1Result == "ROCK🪨" and p2Result == "SCISSORS✂️":
  print("Player 1's ROCK🪨 completely obliterated Player 2's SCISSORS✂️!")
  print("Player 1 WINS round 3!!!")
  round3Results = "P1 WIN"
elif p1Result == "ROCK🪨" and p2Result == "PAPER📄":
  print("Yeesh! Player 1's ROCK🪨 was smothered by Player 2's PAPER📄!")
  print("Player 2 WINS round 3!!!")
  round3Results = "P2 WIN"
elif p1Result == "SCISSORS✂️" and p2Result == "ROCK🪨":
  print("Player 2's ROCK🪨 completely obliterated Player 1's SCISSORS✂️!")
  print("Player 2 WINS round 3!!!")  
  round3Results = "P2 WIN"
elif p1Result == "PAPER📄" and p2Result == "ROCK🪨":
  print("Yeesh! Player 2's ROCK🪨 was smothered by Player 1's PAPER📄!")
  print("Player 1 WINS round 3!!!") 
  round3Results = "P1 WIN"
elif p1Result == "PAPER📄" and p2Result == "PAPER📄":
  print("Both Player 1 and Player 2 picked PAPER📄!") 
  print("It was a tie!")
  round3Results = "TIE"
elif p1Result == "PAPER📄" and p2Result == "SCISSORS✂️":
  print("Wow, Player 2's SCISSORS✂️ absolutely shredded Player 1's PAPER📄!")
  print("Player 2 WINS round 3!!!")
  round3Results = "P2 WIN"
elif p1Result == "SCISSORS✂️" and p2Result == "PAPER📄":
  print("Wow, Player 2's SCISSORS✂️ absolutely shredded Player 1's PAPER📄!")
  print("Player 1 WINS round 3!!!")
  round3Results = "P1 WIN"
else:
  print("Both Player 1 and Player 2 picked SCISSORS✂️!") 
  print("It was a tie!")
  round3Results = "TIE"

#round1 points
if round1Results == "P1 WIN":
  p1r1Points = 1
  p2r1Points = 0

elif round1Results == "P2 WIN":
  p1r1Points = 0
  p2r1Points = 1

else:
  p1r1Points = 0
  p2r1Points = 0


#round2 points
if round2Results == "P1 WIN":
  p1r2Points = 1
  p2r2Points = 0

elif round2Results == "P2 WIN":
  p1r2Points = 0
  p2r2Points = 1

else:
  p1r2Points = 0
  p2r2Points = 0

#round3 points
if round3Results == "P1 WIN":
  p1r3Points = 1
  p2r3Points = 0

elif round3Results == "P2 WIN":
  p1r3Points = 0
  p2r3Points = 1

else:
  p1r3Points = 0
  p2r3Points = 0

p1Points = (p1r1Points + p1r2Points + p1r3Points)

p2Points = (p2r1Points + p2r2Points + p2r3Points)


if p1Points > p2Points:
  print()
  print("In total, Player 1 won",p1Points,"game(s), and Player 2 won",p2Points,"game(s)!")
  print()
  print("Player 1 WINS!!!")
  print("Congratulations, Player 1!")
  print("Better luck next time, Player 2...")

elif p2Points > p1Points:
  print()
  print("In total, Player 1 won",p1Points,"game(s), and Player 2 won",p2Points,"game(s)!")
  print()
  print("Player 2 WINS!!!")
  print("Congratulations, Player 2!")
  print("Better luck next time, Player 2...")

else:
  print()
  print("In total, Player 1 won",p1Points,"game(s), and Player 2 won",p2Points,"game(s)!")
  print()
  print("It's a tie!")
