# Edna Lynn Laxa
# Computer Programming IV
# Assignment: Code Conversion: Language of your choice
# November 17, 2023

# Creating a method for the player menu
def playerMenu():
    print("\nPlayer Selection:")
    print("1. See All Players")
    print("2. See Players with Odd Numbers")
    print("3. Search by first letter of Player's name")
    print("4. Add Player")

# Class placed in the main window , refrence from YT Corey Schafer
class Player:

# init is a method aka constructor known for initializing an instances of classes.
    def __init__(self, first, number):
        self.first = first  #field attribute
        self.number = number #field attribute

# Creating a method , kinda like override to string but this will display the format for players.
    def playerfull(self):
        print(f"Player: {self.first}, Number {self.number}")

# Emptylist for PlayerArray
playersArray = []

# Creating a method dedicated to adding player to the array. In this method, parameter is required for name & number. Defining thePlayer
# to the class of required fields then grabbing the playersArray when pressing . options are prompt, Append is chosen because it method
# that grabs the element to add it to the array.
def playerAdd(first, number):
    thePlayer = Player(first, number)
    playersArray.append(thePlayer)

# 5 players produced
playerAdd('Bella', 1)
playerAdd('Teddy', 2)
playerAdd('Daisy', 3)
playerAdd('Wyland', 4)
playerAdd('Kai', 5)

# for player in playersArray:
#     player.playerfull()

# Aiming for a menu to loop to keep the ball rolling. Made a method dedicated to the menu list to create a cleaner look.
# I learned that the C sharp, console readline is super simple in python its the variable then equal input then the parenthesis.

# print is similar to console write line but predominately uses single quotation instead of double but a double quotation is used when input
# is called which is like console readline

# C sharp in if structure requires parenthesis and brackets but Python is spaced then colon
# for else if it is called elif for PYTHON
# The for each loop is pretty simple to execute in python too. its the keyword for then the variable then the array you like to access

# For literal string in Python it is the letter f but in C sharp it is the money sign.

while True:
    playerMenu()
    print('Select a number from 1- 4')
    userSelection = input("Enter: ")

    if userSelection == "1":
        for player in playersArray:
            player.playerfull()
    elif userSelection == "2":
        for player in playersArray:
         if player.number % 2 != 0:
            player.playerfull()
    elif userSelection == "3":
        print('Search by first letter')
        userLetter = input("Enter Letter: ")
        for player in playersArray:
            if player.first[0] == userLetter:
                player.playerfull()
            else:
                print(f"No player starts with the letter you entered : {userLetter}")
                break;
    elif userSelection == "4":
        print('Add player')
        userName = input ("Enter player name: ")
        userNumber = input ("Enter player number: ")
        playerAdd(userName, userNumber)
        print(f'Player {userName} , Player Number: {userName} joined the TEAM')
        for player in playersArray:
            player.playerfull()

# I learned with Python, spacing is very strict. Things had to align line by line in order for things to be executed.
