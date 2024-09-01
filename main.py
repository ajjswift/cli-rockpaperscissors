# Rock, paper, scisssors program

import random
import os


def lossP2(choice, p1Name, p2Name):
  if (choice == "SCISSORS"):
    print(f"[P1 WIN] {p1Name}'s scissors slice through {p2Name}'s paper")
  elif (choice == "PAPER"):
    print(f"[P1 WIN] {p1Name} encapsulates {p2Name}'s rock with their paper")
  elif (choice == "ROCK"):
    print(f"[P1 WIN] {p1Name}'s rock batters {p2Name}'s scissors")


def lossP1(choice, p1Name, p2Name):
  if (choice == "SCISSORS"):
    print(f"[P2 WIN] {p2Name} cuts {p1Name}'s paper to shreds with their scissors")
  elif (choice == "PAPER"):
    print(f"[P2 WIN] {p2Name} entombs {p1Name}'s rock with their paper")
  elif (choice == "ROCK"):
    print(f"[P2 WIN] {p2Name} rock smashes {p1Name}'s scissors as if it's whack-a-mole")

def draw(choice):
  if (choice == "SCISSORS"):
    print("[DRAW] Scissors can't cut scissors, my friend")
  elif (choice == "PAPER"):
    print("[DRAW] You tryna make a book or smthn? (Paper + Paper)")
  elif (choice == "ROCK"):
    print("[DRAW] Caveman vibes.. Rock and rock make fire 🔥")


while True:
  chosenSuccessfullyP1 = False
  while chosenSuccessfullyP1 != True:
    p1Name = input("[P1] Choose a name: ").capitalize()
    p1Choice = input("[P1] Choose ROCK, PAPER, or SCISSORS: ").upper()
    if (p1Choice == "ROCK") or (p1Choice == "PAPER") or (p1Choice == "SCISSORS"):
      chosenSuccessfullyP1 = True
    else:
      print("[P1] Invalid choice.")

  os.system('clear')
  chosenSuccessfullyP2 = False
  while chosenSuccessfullyP2 != True:
    p2Name = input("[P2] Choose a name: ").capitalize()
    p2Choice = input("[P2] Choose ROCK, PAPER, or Scissors: ").upper()
    if (p2Choice == "ROCK") or (p2Choice == "PAPER") or (p2Choice == "SCISSORS"):
      chosenSuccessfullyP2 = True
    else:
      print("[P2] Invalid choice.")

  
  if (p1Choice == "SCISSORS") and (p2Choice == "PAPER"):
    lossP2(p1Choice, p1Name, p2Name)
  elif (p1Choice == "PAPER") and (p2Choice == "ROCK"):
    lossP2(p1Choice, p1Name, p2Name)
  elif (p1Choice == "ROCK") and (p2Choice == "SCISSORS"):
    lossP2(p1Choice, p1Name, p2Name)
  elif (p2Choice == "SCISSORS") and (p1Choice == "PAPER"):
    lossP1(p2Choice, p1Name, p2Name)
  elif (p2Choice == "PAPER") and (p1Choice == "ROCK"):
    lossP1(p2Choice, p1Name, p2Name)
  elif (p2Choice == "ROCK") and (p1Choice == "SCISSORS"):
    lossP1(p2Choice, p1Name, p2Name)
  elif (p2Choice == p1Choice):
    draw(p2Choice)
  print()