print("Animal Sounds Game")
print()

while exit != "yes":
  
  animal = input("What animal would you like?: ")
  
  if animal == "dog" or animal == "a dog" or animal == "Dog":
    animalSound = "woof"
    
  elif animal == "cat" or animal == "a cat" or animal == "Cat":
    animalSound = "meow"
    
  elif animal == "lion" or animal == "Lion" or animal == "a lion":
    animalSound = "roar"
    
  elif animal == "frog" or animal == "Frog" or animal == "a frog":
    animalSound = "croak"
    
  elif animal == "bee" or animal == "a bee" or animal == "Bee":
    animalSound = "buzz"
    
  elif animal == "dolphin" or animal == "Dolphin" or animal == "a dolphin":
    animalSound = "click"
    
  elif animal == "elephant" or animal == "Elephant" or animal == "an elephant":
    animalSound = "trumpet"
    
  elif animal == "tiger" or animal == "Tiger" or animal == "a tiger":
    animalSound = "growl"
    
  elif animal == "cow" or animal == "Cow" or animal == "a cow":
    animalSound = "moo"

  elif animal == "sheep" or animal == "Sheep" or animal == "a sheep":
    animalSound = "baaa"

  elif animal == "goat" or animal == "Goat" or animal == "a goat":
    animalSound = "maaa"
    
  elif animal == "horse" or animal == "a horse" or animal == "Horse":
    animalSound = "neigh"
    
  elif animal == "pig" or animal == "Pig" or animal == "a pig":
    animalSound = "snort"
    
  elif animal == "goose" or animal == "Goose" or animal == "a goose":
    animalSound = "honk"

  elif animal == "snake" or animal == "Snake" or animal == "a snake":
    animalSound = "hiss"

  elif animal == "hen" or animal == "chicken" or animal == "Chicken" or animal == "a chicken" or animal == "a hen" or animal == "Hen":
    animalSound = "cluck"

  elif animal == "mouse" or animal == "a mouse" or animal == "a mouse":
    animalSound = "squeak"

  elif animal == "duck" or animal == "a duck" or animal == "Duck":
    animalSound = "quack"

  elif animal == "koala" or animal == "a koala" or animal == "Koala":
    animalSound = "bellow"

  elif animal == "wolf" or animal == "a wolf" or animal == "Wolf":
    animalSound = "howl"

  elif animal == "donkey" or animal == "a donkey" or animal == "Donkey":
    animalSound = "hee-haw"

  elif animal == "eagle" or animal == "an eagle" or animal == "Eagle":
    animalSound = "screech"

  elif animal == "owl" or animal == "an owl" or animal == "Owl":
    animalSound = "hoot"

  elif animal == "monkey" or animal == "Monkey" or animal == "a monkey":
    animalSound = "chatter"

  elif animal == "fox" or animal == "Fox" or animal == "a fox":
    animalSound = "Ring-ding-ding-ding-dingeringeding"
    
  else:
    animalSound = "ooblahgloot"

  if animalSound != "ooblahgloot":
    print("The", animal,"goes",animalSound,".")
    print()
  else:
    print("Errr... the", animal, "goes",animalSound,"?")
    print()
    
  exit = input("Do you want to exit?")
  print()
