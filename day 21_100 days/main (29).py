print("Multiplication Game!")
print()
print("Test your multiplication skills in this fun maths game!")
print()
counter = 0
number = int(input("Choose a number/multiple: "))
print()
for i in range(1,13):
  print(number,"x",i,"=")
  guess = int(input(" "))
  print()
  if guess == number * i:
    print("Amazing job! You got it right! 😀")
    counter += 1
  else:
    print("Sorry, you got it wrong. The answer was",number * i)
print()
if counter == 12:
  print("WOW! You got all 12 questions right! A perfect score! 🤩🥳")
else:
  print("You got",counter,"out of 12 questions right.")
