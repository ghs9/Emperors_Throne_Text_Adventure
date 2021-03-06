#Emperor's Throne Pre-Alpha 0.0.01
#Game Core
from Entity import * 
import random
from Environment import *
from Player import *
from Door import *
import EnvironmentGenerator

#Game Intro!
print("Welcome Player!")
name = input("Please Input Your Name! ")
while True:
    try:
        difficulty = int(input("Please Select a Difficulty From 1-5 "))
        if(difficulty>0 and difficulty<6):
            break
    except ValueError:
        print()
#Player initialization
#TODO modify stats based on difficulty
player = Player(name,25,5)
print("\n\n---------------------------------------------------------------------------------------------")
print("Welcome "+name+"! You are about to embark on a great quest which\n is a matter of life and death for the entire kingdom!")
print("Our story begins here:")
print("""
          ___     ___     ___     ___          ___     ___     ___     ___
         |   |   |   |   |   |   |   |        |   |   |   |   |   |   |   |
         |   |   |   |   |   |   |   |        |   |   |   |   |   |   |   |
         |   |___|   |___|   |___|   |________|   |___|   |___|   |___|   |
         |                                                                |
         |            ___                                  ___            |
         |           /   \                                /   \           |
         |          |     |                              |     |          |
         |          |     |                              |     |          |
         |          |_____|                              |_____|          |
         |                        __________________                      |
         |                       /  |  |      |  |  \                     |
         |                      /   |  |      |  |   \                    |
         |                     /    |  |      |  |    \                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |_____|__|______|__|____|                   |""")
input("Press Enter to Continue...")
print("This is your father's castle. Yet your adventure does not start in the throne room, or the dining room, or even your bedroom.")
input("Press Enter to Continue...")
print("You have awoken this morning locked in the jail cell in the cellar of the castle. Surrounded by rats and other undesirables.")
input("Press Enter to Continue...")
print("Your memory slowly returns as you clear the sleep from your eyes...")
print("You remember the violent murder of your father at the hands of your uncle\nYou realize your uncle must have thrown you in the jail to keep you out of the way")
print("until he can fully take over the kingdom!")
input("Press Enter to Continue...")
print("You quickly escape the jail cell and decide to confront your uncle in the throne room!")
input("Press Enter to Continue...")
#Game Starts Here!
#Predefined location, with one potion type random item.
JailCell = Environment([EnvironmentGenerator.genObject(2,difficulty)],"smelly dark room outside your jail cell",[Door(False,"Up",0)])
print(JailCell.toString())

#Testing RunCode
while(1):
    input("Press Enter to Continue...")
    print(EnvironmentGenerator.genEnvironment(difficulty,"Up").toString())

