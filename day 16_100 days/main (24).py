counter = 1
print("Fill in the blank lyrics!")
print()
print("Type in the blank lyrics and see if you are as cool as me.😎")
print()
while True:
  print("Never gonna ____ you up")
  guess = input("")
  if guess != "give":
    counter += 1
  else:
    print("Great job! It only took you","\033[36m",counter,"\033[0m","attempts!")
    break
