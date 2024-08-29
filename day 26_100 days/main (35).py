import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()
  
pause()

def play():
  pygame.mixer.unpause()

def menu():
  print("\033[35m","🎧 Music Player 🎧","\033[0m")
  print()
  print("Press","\033[31m","A","\033[0m","to Play")
  print("Press","\033[32m","B","\033[0m","to Pause")
  print("Press","\033[33m","Y","\033[0m","to See Menu Again")
  print("Press","\033[34m","X","\033[0m","to Exit")

os.system("clear")
menu()
while True:
  userInput = input("What do you want to do? ")

  print()
  if userInput == "A":
    play()
    os.system("clear")
    print("Playing some proper tunes!")
    time.sleep(2)
    os.system("clear")
    
  elif userInput == "B":
    pause()
    os.system("clear")
    
  elif userInput == "Y":
    pause()
    os.system("clear")
    time.sleep(1)
    menu()
    
  elif userInput == "X":
    os.system("clear")
    break

  else:
    os.system("clear")
    print("Invalid Input")
    time.sleep(2)
    menu()
    
