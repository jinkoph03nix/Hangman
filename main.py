#All code is written by me using Python 3.8.2
#All code is written for use as a project in the 2021-2022 AP Computer Science Principles Performance Task

#Hangman Game
import random

def print_figure(strikes): #procedure with parameter "strikes"
  #output based on inputs
  for i in range(6):
    print("_", end = '')
  if (strikes == 10):
    #all letters wrong
    print("")
    print(" |   |")
    print(" |   O")
    print(" | _/|\_")
    print(" | _/ \_")
    print("_|_______")
  elif (strikes == 9):
    print("")
    print(" |   |")
    print(" |   O")
    print(" | _/|\_")
    print(" | _/ \\")
    print("_|_______")
  elif (strikes == 8):
    print("")
    print(" |   |")
    print(" |   O")
    print(" | _/|\_")
    print(" |  / \\")
    print("_|_______")
  elif (strikes == 7):
    print("")
    print(" |   |")
    print(" |   O")
    print(" | _/|\_")
    print(" |  / ")
    print("_|_______")
  elif (strikes == 6):
    print("")
    print(" |   |")
    print(" |   O")
    print(" | _/|\_")
    print(" |")
    print("_|_______")
  elif (strikes == 5):
    print("")
    print(" |   |")
    print(" |   O")
    print(" | _/|\\")
    print(" |")
    print("_|_______")
  elif (strikes == 4):
    print("")
    print(" |   |")
    print(" |   O")
    print(" |  /|\\")
    print(" |")
    print("_|_______")
  elif (strikes == 3):
    print("")
    print(" |   |")
    print(" |   O")
    print(" |  /|")
    print(" |")
    print("_|_______")
  elif (strikes == 2):
    print("")
    print(" |   |")
    print(" |   O")
    print(" |   |")
    print(" |")
    print("_|_______")
  elif (strikes == 1):
    print("")
    print(" |   |")
    print(" |   O")
    print(" |")
    print(" |")
    print("_|_______")
  else:
    #no letters wrong/default
    print("")
    print(" |   |")
    print(" |")
    print(" |")
    print(" |")
    print("_|_______")
  return

#Multiple base arrays with words, based on categories
animals = ["raccoon", "hedgehog", "anteater", "capybara", "tiger", "elephant", "axolotl", "flamingo", "buffalo", "crocodile", "hummingbird", "spider", "leopard", "manatee", "pufferfish"]
programming = ["algorithm", "binary", "hexadecimal", "operator", "network", "functions", "development", "sprites", "variable", "arrays", "software", "compiler", "database", "framework", "interface"]
food = ["asparagus", "avocado", "broccoli", "chocolate", "dumplings", "enchiladas", "hamburger", "lasagna", "milkshake", "quesadilla", "spaghetti", "waffles", "zucchini", "watermelon", "yogurt"]
countries = ["australia", "bangladesh", "cambodia", "ethiopia", "finland", "germany", "ireland", "lithuania", "netherlands", "norway", "philippines", "poland", "romania", "switzerland", "thailand"]
colors = ["alabaster", "amaranth", "amethyst", "aquamarine", "maroon", "cerulean", "crimson", "fuschia", "indigo", "lavender", "turquoise", "orange", "ultramarine", "periwinkle", "sapphire"]

#program-wide variables
categories = [1,2,3,4,5]
replay = True

points = 0

#allows for replaying
while replay == True:
  #Randomly picks category
  category = random.choice(categories)
  word = ""
  catName = ""

  #Randomly picks word (selection)
  if category == 1:
    word = random.choice(animals)
    catName = "Animals"
  elif category == 2:
    word = random.choice(programming)
    catName = "Programming"
  elif category == 3:
    word = random.choice(food)
    catName = "Food"
  elif category == 4:
    word = random.choice(countries)
    catName = "Countries"
  elif category == 5:
    word = random.choice(colors)
    catName = "Colors"

  #Splits word into array (list/collection type)
  answer = list(word)

  #Duplicates array and makes all values an underscore
  shown = ["_" for i in range(len(word))]

  strikes = 0
  loss = False
  win = False

  while (loss == False and win == False):
    print()
    #Prints out stick figure (calls procedure)
    print_figure(strikes)

    """
    Full figure:
    ______
     |   |
     |   O
     | _/|\_
     | _/ \_
    _|_______
    """

    #Prints out category + underscored prompt
    print("Category: " + catName)
    print("Word: " + ' '.join(shown))

    #Player guesses (instruction for input)
    guess = input("Guess a letter: ")

    good = False

    #Checks if letter is in the answer (iteration)
    for i in range(len(answer)):
      if answer[i] == guess.lower():
        #If it is, set the equivalent value in guess
        shown[i] = guess.lower()
        good = True
    
    if (good == False):
      strikes += 1

    #Repeat 10 times or until answer is the guess
    if answer == shown:
      #win game
      points += 1
      win = True
      print()
      print("-----------------")
      print("YOU WIN!")
      print("Points: " + str(points))
      print("-----------------")
      print("Word: " + word)
      print("Strikes: " + str(strikes) + "/10")
      print("-----------------")
      print()
    elif strikes == 10:
      #lose game
      print()
      print("-----------------")
      print()
      print_figure(10) #second procedure call
      loss = True
      print()
      print("-----------------")
      print("YOU LOSE!")
      print("Points: " + str(points))
      print("-----------------")
      print("Word: " + word)
      print("Strikes: " + str(strikes) + "/10")
      print("-----------------")
      print()

  #Replay game prompt
  repeat = input("Want to play again? (y/n):")

  if (repeat == 'y' or repeat == 'Y'):
    replay = True;
  else:
    replay = False;
