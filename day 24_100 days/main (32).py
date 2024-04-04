import random
print("The Super-Cool INFINITY DICE")
sides = int(input("How many sides would you like on your dice?: "))
print()
roll = "yes"

def rolldice(sides):
  print("You rolled", random.randint(1,sides))
  print()
while roll == "yes" or roll == "Yes" or roll == "Yeah" or roll == "yeah" or roll == "sure" or roll == "Sure":
    rolldice(sides)
    roll = input("Would you like to roll again?: ")

print()
print("Thanks for playing! :)")
