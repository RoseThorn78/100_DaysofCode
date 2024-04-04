import random
generate = "yes"

print("\033[35m")
print("Character Health Stats Generator")
print("\033[0m")

while generate == "yes":

  def rolldice(sides):
    return random.randint(1, sides)
    
  def roll():
    dice1 = rolldice(6)
    dice2 = rolldice(8)
    health = dice1 * dice2
    return health

  health = roll()

  if health <= 48 and health >= 41:
    colour = "\033[35m"
  elif health <= 40 and health >= 33:
    colour = "\033[31m"
  elif health <= 32 and health >= 25:
    colour = "\033[33m"
  elif health <= 24 and health >= 17:
    colour = "\033[32m"
  elif health <= 16 and health >= 9:
    colour = "\033[36m"
  else:
    colour = "\033[34m"
    
  print()
  print("\033[33m")
  characterName = input("Name your character: ")
  print("\033[0m")
  print()
  print("Your character,",colour,characterName,"\033[0m","'s health is:",health,"hp")
  print()
  generate = input("Would you like to create another character? (yes/no) : ")
